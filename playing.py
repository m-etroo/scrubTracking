# Setup logging module
import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

# Import other modules
import config
from handlers import api_urls
import requests
import time

# Define main tracking function
def track_players():
    # Get data from Roblox API
    roblox_request = requests.get(api_urls.game_url())

    # Get approximate time of request
    request_time = time.gmtime()
    time_string = time.strftime(config.TIME_FORMAT, request_time)

    # Check for good request
    if roblox_request.status_code == 200:
        logging.info('Roblox game API request successful') # Log
        roblox_data = roblox_request.json() # Get request data
        
        # Parse request data to get number of players
        try:
            players = roblox_data["data"][0]["playing"]
        except KeyError:
            logging.error('Roblox API data does not include playing count, likely an API or request issue - players will not be tracked')
            return

        # Format request data to Discord
        discord_request_json = {
            "content": f"───────────────────\n**{f'{players:,}'}** current players | `{time_string}`"
        }

        # Send request to Discord webhook
        discord_request = requests.post(config.DISCORD_WEBHOOKS['playing'], json=discord_request_json)
        
        # Check for good request
        if discord_request.status_code == 204:
            logging.info('Discord API request successful - playing tracker')
        else:
            logging.error('Discord API request unsuccessful, likely an API or request issue - players will not be tracked')
            return

    else:
        logging.error('Roblox game API request unsuccessful, likely an API or request issue - players will not be tracked')
        return