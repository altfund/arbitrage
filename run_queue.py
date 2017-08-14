import logging
import time

from arbitrage.arbiter import Arbiter
from arbitrage.config import Configuration

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=log_format, level=logging.DEBUG)

config = Configuration()
arbiter = Arbiter(config)

def update(arbiter):
    arbiter.depths = arbiter.update_depths()
    arbiter.tickers()
    arbiter.tick()
    return(arbiter)
    

while 1:
    try:
        arbiter = update(arbiter)
    except:
        pass
    time.sleep(config.refresh_rate)