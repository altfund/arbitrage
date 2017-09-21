from arbitrage.markets._huobi import HuobiBase

class HuobiETH(HuobiBase):
    def __init__(self, config=None):
        super().__init__("BTC", "ethbtc", config)
        
class HuobiLTC(HuobiBase):
    def __init__(self, config=None):
        super().__init__("BTC", "ltcbtc", config)
        