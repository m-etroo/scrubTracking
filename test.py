import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

import os, config
import time, sys, config
import tracker

try:
    #Setting up webhook urls
    config.DISCORD_WEBHOOKS = {
        "visits": os.environ['DEV_WEBHOOK'], 
        "members": os.environ['DEV_WEBHOOK'],
        "playing": os.environ['DEV_WEBHOOK']
    }
    #Actual test
    start = time.time()

    tracker.track("visits")
    tracker.track("members")
    tracker.track("playing")

    duration = time.time() - start
finally:
    logging.critical(f'Critical error: {sys.exc_info()}')
