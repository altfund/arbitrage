import logging
import time

from arbitrage.arbiter import Arbiter
from arbitrage.config import Configuration, SampleConfig

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO) #DEBUG

config = SampleConfig() #Configuration()
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