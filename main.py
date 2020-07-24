import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

import time, sys, config
import tracker

while True:
    try:
        start = time.time()

        tracker.track("visits")
        tracker.track("members")
        tracker.track("playing")

        duration = time.time() - start
        time.sleep(config.INTERVAL - duration)
    except ConnectionError:
        logging.error(f'Error: {sys.exc_info()}')
        time.sleep(config.INTERVAL)