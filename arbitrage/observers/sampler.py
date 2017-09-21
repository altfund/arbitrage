import logging
from arbitrage.observers.observer import ObserverBase

logging.basicConfig(filename='opportunity_log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

LOG = logging.getLogger(__name__)

_format = "profit: %f USD, vol: %f BTC, %s [%s] -> %s [%s], ~%.2f%%"


class Sampler(ObserverBase):
    def opportunity(self, profit, volume, buyprice, kask, sellprice, kbid,
                    perc, weighted_buyprice, weighted_sellprice, max_buy_price, min_sell_price):
        """Log opportunity"""
    

        buy_exchange, buy_currency = kask[:-3], kask[-3:]
        sell_exchange, sell_currency = kbid[:-3], kbid[-3:]
        LOG.info(_format % (profit,
                            buy_currency,
                            volume,
                            buy_exchange.upper(),
                            buy_currency,
                            buyprice,
                            weighted_buyprice,
                            max_buy_price,
                            sell_exchange.upper(),
                            sell_currency,
                            sellprice,
                            weighted_sellprice,
                            min_sell_price,
                            perc#,
                            #kask,
                            #kbid,
                            #weighted_buyprice,
                            #weighted_sellprice
                            ))
