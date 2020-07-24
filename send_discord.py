# Setup logging module
import logging

import requests
from math import ceil
import config
from handlers import prev, milestones, motivation

def send_webhook(request_type, number, time_string):
    mention = ""

    # Determine number since last, but only if visits or members
    if request_type == "visits" or request_type == "members":
        if prev.last_count[request_type] == None:
            pass
        else:
            prev.since_last[request_type] = number - prev.last_count[request_type]
        prev.last_count[request_type] = number

    # Get number to countdown to, but only if visits or members
        countdown_goal = ceil(number/config.COUNTDOWN_FREQUENCY[request_type]) * config.COUNTDOWN_FREQUENCY[request_type]

    # Determine if this should trigger a milestone mention, but only if visits or members
        for milestone in config.VISITS_MILESTONES:
            if number >= int(milestone):
                mention = f"\n<@&{config.MENTION_ROLE_ID}>"
                milestones.remove_milestone("visits", milestone)

    # Get motivation insert, but only if visits
    if request_type == "visits":
        motivation_insert = motivation.set_motivation(number)
    else:
        motivation_insert = ""
    
    # Format request data to Discord
    if request_type == "visits" or request_type == "members":
        l = f' | **{prev.since_last[request_type]}** {request_type} since last count'
        r = f'{countdown_goal - number:,}'
        u = f"{f'{countdown_goal:,}'} {request_type.capitalize()} Countdown"
        
        if request_type == "visits":
            s = "game visits"
            c = f' | **{r}** visits remaining'
        else:
            c = f' | **{r}** members remaining'
            s = "group members"
    else:
        l = ""
        c = ""
        u = "SCR Players Tracker"
        s = "players"
    request_json = {
        "content": f"───────────────────\n**{f'{number:,}'}** {s}{c}{l} | `{time_string}`{motivation_insert}{mention}",
        "username": u
    }

    # Send request to Discord webhook
    request = requests.post(config.DISCORD_WEBHOOKS[request_type], json=request_json)

    # Check for good request
    if request.status_code == 204:
        logging.info(f'Discord API request successful - {request_type} tracker')
    else:
        logging.error(f'Discord API request unsuccessful, likely an API or request issue - {request_type} will not be tracked')
        return