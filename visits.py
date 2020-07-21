# Setup logging module
import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

# Import other modules
import config, prev
import requests
import time
from math import ceil

# Define main tracking function
def track_visits():
    # Get data from Roblox API
    roblox_request = requests.get(config.GAME_REQUEST_URL)

    # Get approximate time of request
    request_time = time.gmtime()
    time_string = time.strftime(config.TIME_FORMAT, request_time)

    # Check for good request
    if roblox_request.status_code == 200:
        logging.info('Roblox game API request successful') # Log
        roblox_data = roblox_request.json() # Get request data
        
        # Parse request data to get number of visits
        try:
            visits = roblox_data["data"][0]["visits"]

            # Determine since last
            if prev.last_count["visits"] == None:
                pass
            else:
                prev.since_last["visits"] = visits - prev.last_count["visits"]
            prev.last_count["visits"] = visits

        except KeyError:
            logging.error('Roblox API data does not include visits count, likely an API or request issue - visits will not be tracked')
            return

        # Get number to countdown to
        countdown_goal = ceil(visits/config.MEMBERS_COUNTDOWN) * config.MEMBERS_COUNTDOWN

        # Format request data to Discord
        l = prev.since_last["visits"]
        discord_request_json = {
            "content": f"───────────────────\n**{f'{visits:,}'}** game visits | **{f'{countdown_goal - visits:,}'}** visits remaining | **{l}** visits since last count | `{time_string}`",
            "username": f"{f'{countdown_goal:,}'} Visits Countdown"
        }

        # Send request to Discord webhook
        discord_request = requests.post(config.DISCORD_WEBHOOKS['visits'], json=discord_request_json)
        
        # Check for good request
        if discord_request.status_code == 204:
            logging.info('Discord API request successful - visits countdown')
        else:
            logging.error('Discord API request unsuccessful, likely an API or request issue - visits will not be tracked')
            return

    else:
        logging.error('Roblox game API request unsuccessful, likely an API or request issue - visits will not be tracked')
        return
