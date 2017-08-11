import os
import configparser

from arbitrage import registry


class ConfigBase(object):
    def __init__(self):
        self.opts = []


class RabbitmqCfgMixin(ConfigBase):
    """Represent required for the :Rabbitmq observer configs"""

    def __init__(self):
        super().__init__()
        
        config = configparser.ConfigParser()
        config.read('config')

        default_queue = config['settings']['queue_url']
        self.amqp_url = os.getenv('CLOUDAMQP_URL', default_queue)
        self.report_queue = "orders.queue"
        self.queue_args = {"x-dead-letter-exchange": "orders.dead-letter.queue"} #None
        self.opts.extend(['report_queue', 'amqp_url', 'queue_args'])
        default_key = 1
        default_endpoint = "http://localhost:8000/api/arbitrage_opportunity/"
        self.api_endpoint = os.getenv('API_ENDPOINT', default_endpoint)
        self.api_key = os.getenv('API_KEY', default_key)
        self.creds = {s:dict(config.items(s)) for s in config.sections()}
        self.max_tx_volume = float(config['settings']['max_tx_volume'])


class Configuration(RabbitmqCfgMixin):
    """Represent the minimal config opts required for the :Arbiter"""

    def __init__(self):
        self.opts = []

        super().__init__()
        self.refresh_rate = 5
        self.default_market_update_rate = 1
        self.transaction_cost = 0 #0.003
        self.market_expiration_time = 120
        #self.max_tx_volume = 0.005
        self.observers = ['Logger', 'Rabbitmq']
        self.markets = list(registry.markets_registry.keys()) #["GDAXUSD", "KrakenUSD", "GDAXLTC","KrakenLTC", "KrakenETH", "GDAXETH"]
        self.opts.extend([
            'default_market_update_rate',
            'market_expiration_time',
            'fiat_update_delay',
            'max_tx_volume',
            'refresh_rate',
            'observers',
            'bank_fee',
            'markets'
        ])
        

    def as_dict(self):
        """Returns dict representation of the configuration opts"""
        return {k: getattr(self, k, None) for k in self.opts}

    def update(self, config: dict):
        """Update configuration values from :config"""
        for key in config:
            setattr(self, key, config.get(key))
        return self

class SampleConfig(ConfigBase):
    def __init__(self):
        self.opts = []

        super().__init__()
        self.refresh_rate = 30
        self.default_market_update_rate = 30
        self.transaction_cost = .003
        self.market_expiration_time = 120
        self.max_tx_volume = 10
        self.observers = ['Logger']
        self.markets = ["GDAXUSD", "KrakenUSD", "GDAXLTC","KrakenLTC", "KrakenETH", "GDAXETH"]
        self.opts.extend([
            'default_market_update_rate',
            'market_expiration_time',
            'fiat_update_delay',
            'max_tx_volume',
            'refresh_rate',
            'observers',
            'bank_fee',
            'markets'
        ])

    def as_dict(self):
        """Returns dict representation of the configuration opts"""
        return {k: getattr(self, k, None) for k in self.opts}

    def update(self, config: dict):
        """Update configuration values from :config"""
        for key in config:
            setattr(self, key, config.get(key))
        return self