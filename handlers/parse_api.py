# Setup logging module
import logging

def parse(request_type, data):
    try:
        if request_type == "visits" or request_type == "motivation":
            number = data["data"][0]["visits"]
        elif request_type == "members":
            number = data["memberCount"]
        elif request_type == "playing":
            number = data["data"][0]["playing"]
        return number # Return number

    except KeyError: # If parse fails
        logging.error(f'Roblox API data does not include {request_type} count, likely an API or request issue - {request_type} will not be tracked')