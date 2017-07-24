import logging
import time

from arbitrage.arbiter import Arbiter
from arbitrage.config import Configuration

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)

config = Configuration()
arbiter = Arbiter(config)

while 1:
    arbiter.depths = arbiter.update_depths()
    arbiter.tickers()
    arbiter.tick()
    time.sleep(config.refresh_rate)