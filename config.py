import configparser
config = configparser.RawConfigParser()
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

# Motivation
MOTIVATON_UNIVERSE_ID = config["motivation"]["game_universe_id"]
MOTIVATION_INFORMAL_NAME = config["motivation"]["game_informal_name"]
MOTIVATIONAL_MESSAGES = open("motivation_messages.txt", "r").readlines()
if MOTIVATON_UNIVERSE_ID != "":
    MOTIVATION_ENABLED = True
else:
    MOTIVATION_ENABLED = False

# Countdown frequency
COUNTDOWN_FREQUENCY = {
    "visits": int(config["countdowns"]["visits_milestone_freq"]),
    "members": int(config["countdowns"]["members_milestone_freq"])
}

# Other
INTERVAL = int(config["time"]["interval"])