from arbitrage.markets._kraken import KrakenBase


class KrakenETH(KrakenBase):
    def __init__(self, config=None):
        super().__init__("BTC", "XETHXXBT", config)

class KrakenEUR(KrakenBase):
    def __init__(self, config=None):
        super().__init__("EUR", "XXBTZEUR", config)
        
class KrakenLTC(KrakenBase):
    def __init__(self, config=None):
        super().__init__("BTC", "XLTCXXBT", config)
        
class KrakenUSD(KrakenBase):
    def __init__(self, config=None):
        super().__init__("USD", "XXBTZUSD", config)
        
class KrakenXLM(KrakenBase): # XLM
    def __init__(self, config=None):
        super().__init__("BTC", 'XXLMXXBT', config)
        
class KrakenREP(KrakenBase): #REP
    def __init__(self, config=None):
        super().__init__("BTC", 'XREPXXBT', config)
        
class KrakenEOS(KrakenBase): #EOS
    def __init__(self, config=None):
        super().__init__("BTC", 'EOSXBT', config)
        
class KrakenGNO(KrakenBase): #GNO
    def __init__(self, config=None):
        super().__init__("BTC", 'GNOXBT', config)
        
class KrakenXRP(KrakenBase): #XRP
    def __init__(self, config=None):
        super().__init__("BTC", 'XXRPXXBT', config)
        
class KrakenICN(KrakenBase): #ICN
    def __init__(self, config=None):
        super().__init__("BTC", 'XICNXXBT', config)

class KrakenZEC(KrakenBase): #ZEC
    def __init__(self, config=None):
        super().__init__("BTC", 'XZECXXBT', config)
        
class KrakenETC(KrakenBase): #ETC
    def __init__(self, config=None):
        super().__init__("BTC", 'XETCXXBT', config)
        
class KrakenXDG(KrakenBase): #XDG
    def __init__(self, config=None):
        super().__init__("BTC", 'XICNXXBT', config)
        
class KrakenDSH(KrakenBase): #DASH
    def __init__(self, config=None):
        super().__init__("BTC", 'DASHXBT', config)
        
class KrakenMLN(KrakenBase):
    def __init__(self, config=None):
        super().__init__("BTC", 'XMLNXXBT', config)
        
class KrakenXMR(KrakenBase):
    def __init__(self, config=None):
        super().__init__("BTC", 'XXMRXXBT', config)

