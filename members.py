# Setup logging module
import logging
logging.basicConfig(filename='countdown.log', filemode='w', format='%(asctime)s:%(levelname)s:%(message)s')

# Import other modules
import config, prev
import requests
import time
from math import ceil

# Define main tracking function
def track_members():
    # Get data from Roblox API
    roblox_request = requests.get(config.MEMBERS_REQUEST_URL)

    # Get approximate time of request
    request_time = time.gmtime()
    time_string = time.strftime(config.TIME_FORMAT, request_time)

    # Check for good request
    if roblox_request.status_code == 200:
        logging.info('Roblox group API request successful') # Log
        roblox_data = roblox_request.json() # Get request data
        
        # Parse request data to get number of members
        try:
            members = roblox_data["memberCount"]

            # Determine since last
            if prev.last_count["members"] == None:
                pass
            else:
                prev.since_last["members"] = members - prev.last_count["members"]
            prev.last_count["members"] = members

        except KeyError:
            logging.error('Roblox API data does not include members count, likely an API or request issue - members will not be tracked')
            return

        # Get number to countdown to
        countdown_goal = ceil(members/config.MEMBERS_COUNTDOWN) * config.MEMBERS_COUNTDOWN
        
        # Format request data to Discord
        l = prev.since_last["members"]
        discord_request_json = {
            "content": f"───────────────────\n**{f'{members:,}'}** group members | **{f'{countdown_goal - members:,}'}** members remaining | **{l}** members since last count | `{time_string}`"
        }

        # Send request to Discord webhook
        discord_request = requests.post(config.DISCORD_WEBHOOKS['members'], json=discord_request_json)
        
        # Check for good request
        if discord_request.status_code == 204:
            logging.info('Discord API request successful - members countdown')
        else:
            logging.error('Discord API request unsuccessful, likely an API or request issue - members will not be tracked')
            return

    else:
        logging.error('Roblox group API request unsuccessful, likely an API or request issue - members will not be tracked')
        return
