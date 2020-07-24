# Setup logging module
import logging

import requests, time
import config
from handlers import api_urls, parse_api

def parse_roblox(request_type):
    # Get data from Roblox API
    try:
        request = requests.get(api_urls.url(request_type))
    except ConnectionError:
        logging.error(f'Roblox {request_type} API request unsuccessful, likely an API or request issue - players will not be tracked')
        return;
    # Get approximate time of request
    request_time = time.gmtime()
    time_string = time.strftime(config.TIME_FORMAT, request_time)
    
    # Check for good request
    if request.status_code == 200:
        logging.info(f'Roblox {request_type} API request successful') # Log
        data = request.json() # Get request data
    else:
        logging.error(f'Roblox {request_type} API request unsuccessful, likely an API or request issue - players will not be tracked')
        return

    # Parse request data to get number
    number = parse_api.parse(request_type, data)

    return number, time_string