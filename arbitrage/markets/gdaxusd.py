from arbitrage.markets._gdax import GDAX


class GDAXUSD(GDAX):
    def __init__(self, config=None):
        super().__init__("USD", "BTC-USD", config)
