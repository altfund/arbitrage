import logging
from arbitrage.observers.observer import ObserverBase

LOG = logging.getLogger(__name__)

_format = "profit: %.8f %s, vol: %f BTC, buy on %s [%s] @ %.8f / %.8f / %.8f -> sell on %s [%s] @ %f / %f / %f, ~%.2f%%"


class Logger(ObserverBase):
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
