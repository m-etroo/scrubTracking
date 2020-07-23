import config

def url(request_type):
    if request_type == "visits" or request_type == "playing":
        uid = config.GAME_UNIVERSE_ID
        return f'https://games.roblox.com/v1/games?universeIds={uid}'
    elif request_type == "members":
        gid = config.GROUP_ID
        return f'https://groups.roblox.com/v1/groups/{gid}'