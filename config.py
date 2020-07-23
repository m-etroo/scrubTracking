import configparser
config = configparser.ConfigParser()
config.read("config.cfg")

# Roblox game
GAME_UNIVERSE_ID = config["game"]["game_universe_id"]

# Roblox group
GROUP_ID = config["group"]["group_id"]

# Discord webhook
DISCORD_WEBHOOKS = {
    "visits": config["webhook"]["visits_webhook"],
    "members": config["webhook"]["members_webhook"],
    "playing": config["webhook"]["playing_webhook"]
}
TIME_FORMAT = config["webhook"]["time_format"]

# Milestones
MENTION_ROLE_ID = config["milestones"]["mention_role_id"]
VISITS_MILESTONES = open("visits_milestones.txt", "r").readlines() # Edit from visits_milestones.txt
MEMBERS_MILESTONES = open("members_milestones.txt", "r").readlines() # Edit from members_milestones.txt

# Countdown frequency
VISITS_COUNTDOWN = config["countdiwns"]["visits_milestone_freq"]
MEMBERS_COUNTDOWN = config["countdiwns"]["members_milestone_freq"]

# Other
INTERVAL = config["time"]["interval"]