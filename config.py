# Roblox game information
GAME_UNIVERSE_ID = 300039023 # Universe id of game to track
GAME_REQUEST_URL = f'https://games.roblox.com/v1/games?universeIds={GAME_UNIVERSE_ID}'

# Roblox group information
GROUP_ID = 3620943 # Group id of group to track
MEMBERS_REQUEST_URL = f'https://groups.roblox.com/v1/groups/{GROUP_ID}'

# Webhook info
DISCORD_WEBHOOKS = { # Dictionary of webhooks to send requests to
    "visits": "", # Visits webhook
    "members": "", # Members webhook
    "playing": "" # Playing webhook
}
MENTION_ROLE_ID = 999999999999999999 # Role id of role to mention for milestones
VISITS_MILESTONES = open("visits_milestones.txt", "r").readlines() # Edit from visits_milestones.txt
MEMBERS_MILESTONES = open("members_milestones.txt", "r").readlines() # Edit from members_milestones.txt

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ" # Time format for tracker time on Discord
VISITS_COUNTDOWN = 1000000 # Milestone frequency (count down to every x number of visits)
MEMBERS_COUNTDOWN = 10000 # Milestone frequency (count down to every x number of members)

# Other
INTERVAL = 60 # Number of seconds between tracking requests






# ==================================================================================================
# Do not modify below here
# ==================================================================================================
def remove_milestone(ms_type, milestone):
    if ms_type == "visits":
        VISITS_MILESTONES.remove(milestone) # Removes from current session list

        # Removes for future runs of the script
        milestones = open("visits_milestones", "r").readlines()
        new_text = []
        for line in milestones:
            if milestone not in line:
                new_text.append(milestone)
        
        milestones = open("visits_milestones", "w")
        milestones.writelines(new_text)

    elif ms_type == "members":
        MEMBERS_MILESTONES.remove(milestone) # Removes from current session list
        
        # Removes for future runs of the script
        milestones = open("members_milestones", "r").readlines()
        new_text = []
        for line in milestones:
            if milestone not in line:
                new_text.append(milestone)
        
        milestones = open("members_milestones", "w")
        milestones.writelines(new_text)