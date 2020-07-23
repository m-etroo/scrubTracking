import logging

import requests, random
from handlers import parse_api, api_urls
import config

messages = config.MOTIVATIONAL_MESSAGES

def set_motivation(tracker_visits):
    if config.MOTIVATION_ENABLED == True:
        # Get data from Roblox API
        request = requests.get(api_urls.motivation_url())

        # Check for good request
        if request.status_code == 200:
            logging.info(f'Roblox visits API request successful (motivation)') # Log
            data = request.json() # Get request data
        else:
            logging.error(f'Roblox visits API request unsuccessful, likely an API or request issue - motivation will not be tracked')
            return ""
        
        # Parse request data to get number
        motivation_visits = parse_api.parse("motivation", data)

        times = str(round(motivation_visits / tracker_visits, 3))

        message = messages[random.randint(0, len(messages)-1)]
        insert = f"\n\n**{config.MOTIVATION_INFORMAL_NAME}** has **{times}x** the number of visits you have! {message}"
        return insert
    else:
        return ""