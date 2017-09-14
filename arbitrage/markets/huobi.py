from arbitrage.markets._gdax import HuobiBase

class GDAXETH(GDAXBase):
    def __init__(self, config=None):
        super().__init__("BTC", "ETH-BTC", config)
        
class GDAXEUR(GDAXBase):
    def __init__(self, config=None):
        super().__init__("EUR", "BTC-EUR", config)
        
class GDAXLTC(GDAXBase):
    def __init__(self, config=None):
        super().__init__("BTC", "LTC-BTC", config)
        
class GDAXUSD(GDAXBase):
    def __init__(self, config=None):
        super().__init__("USD", "BTC-USD", config)