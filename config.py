from environs import Env
env = Env()
env.read_env()

# Roblox game information
GAME_UNIVERSE_ID = 300039023 # Universe id of game to track
GAME_REQUEST_URL = f'https://games.roblox.com/v1/games?universeIds={GAME_UNIVERSE_ID}'

# Roblox group information
GROUP_ID = 3620943 # Group id of group to track
MEMBERS_REQUEST_URL = f'https://groups.roblox.com/v1/groups/{GROUP_ID}'

# Webhook info
DISCORD_WEBHOOKS = { # Dictionary of webhooks to send requests to
    "visits": env("VISITS_WEBHOOK"), # Edit from .env file
    "members": env("MEMBERS_WEBHOOK"), # Edit from .env file
    "playing": env("PLAYING_WEBHOOK") # Edit from .env file
}
TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ" # Time format for tracker time on Discord
VISITS_COUNTDOWN = 14000000 # Number of visits to countdown to
MEMBERS_COUNTDOWN = 80000 # Number of members to countdown to

# Other
INTERVAL = 60 # Number of seconds between tracking requests