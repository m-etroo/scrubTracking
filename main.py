import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

import time, sys, config
import tracker

try:
    while True:
        start = time.time()

        tracker.track("visits")
        tracker.track("members")
        tracker.track("playing")

        duration = time.time() - start
        time.sleep(config.INTERVAL - duration)
except ConnectionError:
    time.sleep(config.INTERVAL)
finally:
    logging.critical(f'Critical error: {sys.exc_info()}')