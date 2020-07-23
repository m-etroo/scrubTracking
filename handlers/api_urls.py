import config

def game_url():
    uid = config.GAME_UNIVERSE_ID
    return f'https://games.roblox.com/v1/games?universeIds={uid}'

def group_url():
    gid = config.GROUP_ID
    return f'https://groups.roblox.com/v1/groups/{gid}'