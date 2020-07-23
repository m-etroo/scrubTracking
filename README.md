# scrubTracking
A tool created to track a Roblox game &amp; group, sending stats about those to a Discord webhook. Originally designed for Stepford County Railway on Roblox.

## Setup
### config.cfg
Simply add or replace the values after the equals sign.
* `game_universe_id`: Roblox universe id of the Roblox game to track stats (visits and current players) for. You can obtain the universe id through the Roblox API. Defaults to Stepford County Railway's universe id.
* `group_id`: Roblox group id of the Roblox group to track stats (group members) for, typically the group associated with the game. You can obtain the group id by looking in the group URL. Defaults to Stepford County Railway's group id.
* `visits_webhook`, `members_webhook`, `playing_webhook`: Discord webhook URLs to send requests to when logging game and group statistics. You can use three separate webhooks or the same one, but if you use the same one then all stats will be posted in the same channel.
* `time_format`: Time format string for Python's time formatting. Defaults to ISO 8601.
* `mention_role_id`: Discord role id of the role to mention for milestone announcements. Leave blank if not using milestone announcements. You can copy the role id by right clicking on the role in the mini profile and selecting "Copy ID".
* `visits_milestone_freq`, `members_milestone_frequency`: The milestone frequency for visits and members, respectively. In other words, a milestone will be triggered every x visits/members (starting from 0). So, if the frequency is set to 1,000, for example, a milestone will be triggered at 1,000, 2,000, 3,000, etc.
* `interval`: The time to wait in between tracker requests. So, stats will be posted every x seconds.
### Setting milestones
To receive milestone mentions on Discord, you will need to specify milestones to mention for. This is done in the `visits_milestones.txt` and `members_milestones.txt` files.

Each on a separate line, specify integer milestones to mention on Discord for. Visits milestones go in `visits_milestones.txt` and `members_milestones.txt`. The trackers will automatically remove milestones that have passed and users have been mentioned for.

To disable milestone mentions, leave these files blank.
### Installing required packages
With Python installed, you will need to ensure that all required packages are installed.
* Open the command line.
* Navigate to the directory which has the `requirements.txt` file.
* In the command line, run the following command to install packages: `pip install -r requirements.txt`.

## Running the trackers
After setting up and with Python installed, run the `main.py` file. That's it! The webhook will run at the specified interval. Any error information will be logged in the `countdown.log` file for you to view. Note that there is not yet error handling for incorrect config values, so make sure to enter these correctly.