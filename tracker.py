# Import other modules
import config
from handlers import api_urls
import requests
import time

import get_roblox
import send_discord

# Define main tracking function
def track(request_type):
    number, time_string = get_roblox.parse_roblox(request_type)
    send_discord.send_webhook(request_type, number, time_string)