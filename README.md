# scrubTracking
A tool created to track a Roblox game &amp; group, sending stats about those to a Discord webhook. Originally designed for Stepford County Railway on Roblox.

## Setup
* First, ensure Python is installed, and open the command line. Navigate to the scrubTracking directory and run this pip command: `pip install -r requirements.txt`. This will install all required Python packages.
 * Note: if you already have all the packages listed in `requirements.txt` installed, no need to do this step. Alternatively, you can also install each package one by one.
* Open the `config.py` file to edit it. This file has predefined values that are set for Stepford County Railway, but you can change them for a different game and group.
* Go to line 2, where you can edit the `GAME_UNIVERSE_ID` constant to your own game if you wish. Default is SCR.
* Then, skip to line 6 and edit `GROUP_ID` if you want a different group. Again, default is SCR.
* Skip over the next few lines to line 11. Here, you will enter your Discord webhook URLs. You will need to generate 3 Discord webhooks, one each for visits, members, and players. Copy and paste them between the quotes in the corresponding spots.
* Line 15 has the `MENTION_ROLE_ID` constant. Here, replace the default with an integer Discord role id for the role that should be mentioned when a milestone is reached. If you don't want milestones, leave it as the default and see below.
* Next, there are two lines for milestones - lines 16 and 17. You shouldn't edit these right from here. Instead, go to the two `visits_milestones.txt` and `members_milestones.txt`. In these files, add integer numbers (each on separate lines) of visits/group members that should trigger a role mention to the milestone notification role specific with the `MENTION_ROLE_ID` constant back in `config.py`. If you don't want role pings, you can just leave the role id as the default and leave the other two files blank.
* Go to line 19 and decide if you want to change the time format. By default, ISO 8601 is used (YYYY-MM-DDTHH:MM:SSZ), but you can change this. (See this: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
* The next two lines, 20 and 21, are for the countdown. For game visits and group members, this number is the frequency of the milestones that will be counted down to. So, for example, if the frequency is 1,000,000, the tracker will countdown to each subsequent million (1 million, 2 million, etc.).
* Finally, line 24 is the interval, or how often you would like the webhook to display stats. 60 seconds is the default.
* Don't touch anything below the interval! This code is required for milestone mentions to work properly!

## Running the trackers
After setting up and with Python installed, run the `main.py` file. That's it! The webhook will run at the specified interval. Any error information will be logged in the `countdown.log` file for you to view. Note that there is not yet error handling for incorrect config values, so make sure to enter these correctly.
