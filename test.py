import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

import os, config
import time, sys, config
import visits, members, playing

try:
    config.DISCORD_WEBHOOKS = {
        "visits": os.environ['DEV_WEBHOOK'], 
        "members": os.environ['DEV_WEBHOOK'],
        "playing": os.environ['DEV_WEBHOOK']
    }
    start = time.time()
    
    visits.track_visits()
    members.track_members()
    playing.track_players()

    duration = time.time() - start
    time.sleep(config.INTERVAL - duration)
finally:
    logging.critical(f'Critical error: {sys.exc_info()}')