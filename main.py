import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

import time, sys, config
import visits, members, playing

try:
    while True:
        start = time.time()

        visits.track_visits()
        members.track_members()
        playing.track_players()

        duration = time.time() - start
        time.sleep(config.INTERVAL - duration)
finally:
    logging.critical(f'Critical error: {sys.exc_info()}')