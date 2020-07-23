import config

def remove_milestone(ms_type, milestone):
    if ms_type == "visits":
        config.VISITS_MILESTONES.remove(milestone) # Removes from current session list

        # Removes for future runs of the script
        milestones = open("visits_milestones.txt", "r").readlines()
        new_text = []
        for line in milestones:
            if milestone not in line:
                new_text.append(milestone)
        
        milestones = open("visits_milestones.txt", "w")
        milestones.writelines(new_text)

    elif ms_type == "members":
        config.MEMBERS_MILESTONES.remove(milestone) # Removes from current session list
        
        # Removes for future runs of the script
        milestones = open("members_milestones.txt", "r").readlines()
        new_text = []
        for line in milestones:
            if milestone not in line:
                new_text.append(milestone)
        
        milestones = open("members_milestones.txt", "w")
        milestones.writelines(new_text)