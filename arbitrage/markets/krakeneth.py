from arbitrage.markets._kraken import KrakenBase


class KrakenETH(KrakenBase):
    def __init__(self, config=None):
        super().__init__("ETH", "XXBTZETH", config)
