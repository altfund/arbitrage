from arbitrage.markets._poloniex import PoloniexBase


class PoloniexETH(PoloniexBase):
    def __init__(self, config=None):
        super().__init__("BTC", "BTC_ETH", config)

class PoloniexLTC(PoloniexBase):
    def __init__(self, config=None):
        super().__init__("BTC", "BTC_LTC", config)

#class PoloniexXLM(PoloniexBase): # XLM
#    def __init__(self, config=None):
#        super().__init__("BTC", 'BTC_XLM', config)
        
class PoloniexREP(PoloniexBase): #REP
    def __init__(self, config=None):
        super().__init__("BTC", 'BTC_REP', config)
        
#class PoloniexEOS(PoloniexBase): #EOS
#    def __init__(self, config=None):
#        super().__init__("BTC", 'BTC_EOS', config)
        
class PoloniexGNO(PoloniexBase): #GNO
    def __init__(self, config=None):
        super().__init__("BTC", 'BTC_GNO', config)
        
class PoloniexXRP(PoloniexBase): #XRP
    def __init__(self, config=None):
        super().__init__("BTC", 'BTC_XRP', config)
        
#class PoloniexICN(PoloniexBase): #ICN
#    def __init__(self, config=None):
#        super().__init__("BTC", 'BTC_ICN', config)

class PoloniexZEC(PoloniexBase): #ZEC
    def __init__(self, config=None):
        super().__init__("BTC", 'BTC_ZEC', config)
        
class PoloniexETC(PoloniexBase): #ETC
    def __init__(self, config=None):
        super().__init__("BTC", 'BTC_ETC', config)
        
#class PoloniexXDG(PoloniexBase): #XDG
#    def __init__(self, config=None):
#        super().__init__("BTC", 'BTC_ICN', config)
        
class PoloniexDSH(PoloniexBase): #DASH
    def __init__(self, config=None):
        super().__init__("BTC", 'BTC_DASH', config)
        
#class PoloniexMLN(PoloniexBase):
#    def __init__(self, config=None):
#        super().__init__("BTC", 'BTC_MLN', config)
        
class PoloniexXMR(PoloniexBase):
    def __init__(self, config=None):
        super().__init__("BTC", 'BTC_XMR', config)
