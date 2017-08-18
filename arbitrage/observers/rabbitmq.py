# Copyright (C) 2017, Kirill Bespalov <k.besplv@gmail.com>

import json
import logging
import time

import tenacity
import pika
import requests

from pika.exceptions import AMQPError, AMQPChannelError
from tenacity import stop_after_delay, wait_exponential
from arbitrage.observers.observer import ObserverBase

LOG = logging.getLogger(__name__)


class AMQPClient(object):
    """Represents the AMQP client to send an opportunity given by watcher"""

    def __init__(self, config):
        self.config = config
        self.message_ttl = str(self.config.market_expiration_time * 1000)
        self.report_queue = self.config.report_queue
        self.params = pika.URLParameters(self.config.amqp_url)
        self.queue_args = self.config.queue_args
        self._connection = None
        self._channel = None

    def _queue_exists(self):
        """Check if the queue exists"""
        try:
            self._channel.queue_declare(self.config.report_queue, passive=True)
        except AMQPChannelError as e:
            # restore a channel
            self._channel = self._connection.channel()
            code = e.args[0]
            if code == 404:
                return False
            else:
                raise
        return True

    def ensure_connected(self):
        """Ensure that connection is established and the queue is declared"""
        try:
            if not self._connection or not self._connection.is_open:
                self._connection = pika.BlockingConnection(self.params)
            if not self._channel or not self._connection.is_open:
                self._channel = self._connection.channel()
                if not self._queue_exists():
                    self._channel.queue_declare(self.config.report_queue,
                                                arguments=self.queue_args)

        except AMQPError as e:
            LOG.error('Failed to establish connection. Retrying %s' % e)
            raise
        LOG.debug('AMQP connection to %s was successfully established' %
                  self.config.amqp_url)
        return True

    @property
    def channel(self):
        if not self._connection or not self._channel.is_open:
            stop = stop_after_delay(self.config.market_expiration_time)
            wait = wait_exponential(max=5)
            retry = tenacity.retry(stop=stop, wait=wait)
            retry(self.ensure_connected)()

        return self._channel

    def push(self, data):
        """Push a data to the exchange"""
        try:
            properties = pika.BasicProperties(
                content_type='application/json',
                expiration=self.message_ttl,
                timestamp=int(time.time())
            )
            self.channel.basic_publish(exchange='',
                                       routing_key=self.report_queue,
                                       body=json.dumps(data),
                                       properties=properties)
        except Exception as e:
            LOG.error('Failed to push a message %s. Skipped.' % data)
            


class Rabbitmq(ObserverBase):
    """Represent AMQP based arbitrage opportunity observer"""

    def __init__(self, config):
        super().__init__(config)
        self.client = AMQPClient(config)

    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid,
                    perc, weighted_buyprice, weighted_sellprice, max_buy_price, min_sell_price):
        """Sends opportunity to a message queue"""
        LOG.debug("sending message to queue")
        # split market name and currency:  KrakenUSD -> (Kraken, USD)
        buy_exchange, buy_currency = kask[:-3], kask[-3:]
        sell_exchange, sell_currency = kbid[:-3], kbid[-3:]
        
        #url = "http://localhost:8000/api/arbitrage_opportunity/"
        if sell_currency != buy_currency:
            LOG.info("Sell currency not equal to buy currency")
            return(0)
        
        watch_currency = sell_currency
        
        
        if watch_currency == "DSH":
            watch_currency = "DASH"
        
        data = {
            "api_key":self.client.config.api_key,
            "arb_volume": volume,
            "buy_currency": buy_currency,
            "buy_exchange": buy_exchange.upper(),
            "sell_currency": sell_currency,
            "sell_exchange": sell_exchange.upper(),
        }
        


        #request = requests.post(self.client.config.api_endpoint, data=data)
        #request.content
        #for account in requests.content:
        
        
        creds = self.client.config.creds
        
        #order = {
        #    "params":{
        #        "order_type": "inter_exchange_arb" #_id":
        #        "base_currency": 1#base_currency #_id":
        #        "quote_currency": 1#quote_currency #_id":
        #        "direction": "BID"
        #        "price": weighted_buyprice
        #        "volume": volume
        #    },
        #    "user":{
        #        "id": 1
        #        "investment_strategy":1
        #    }
        #    "exchange":{
        #        "key": 1
        #        "secret": 1
        #        "passphrase": 1
        #    }
        #}
        
        base_currency = "BTC"
        max_tx_volume = 0.001
        
        
        buy_base_currency = watch_currency
        buy_quote_currency = "BTC"
        sell_base_currency = watch_currency
        sell_quote_currency = "BTC"
        
        if watch_currency == "USD" or watch_currency == "EUR":
            buy_base_currency = "BTC"
            sell_base_currency = "BTC"
            buy_quote_currency = watch_currency
            sell_quote_currency = watch_currency
            
        #if buy_base_currency == base_currency:
            # implement volume limit on 
        

        message = {"order_type": "inter_exchange_arb",
                   "order_specs": {
                       "buy_base_currency": buy_base_currency,
                       "buy_quote_currency": buy_quote_currency,
                       "buy_volume": volume,
                       "buy_price": max_buy_price,
                       "buy_exchange": buy_exchange.upper(),
                       "sell_base_currency": sell_base_currency,
                       "sell_quote_currency": sell_quote_currency,
                       "sell_volume": volume,
                       "sell_price": min_sell_price,
                       "sell_exchange": sell_exchange.upper()},
                    "user_specs": {
                        "user_id":1,
                        "investment_strategy_id": 1,
                       "sell_exchange_key": creds[sell_exchange.upper()]['key'],
                       "sell_exchange_secret": creds[sell_exchange.upper()]['secret'],
                       "sell_exchange_passphrase": creds[sell_exchange.upper()]['passphrase'],
                       "buy_exchange_key": creds[buy_exchange.upper()]['key'],
                       "buy_exchange_secret": creds[buy_exchange.upper()]['secret'],
                       "buy_exchange_passphrase": creds[buy_exchange.upper()]['passphrase']
                   },
                   }

        self.client.push(message)