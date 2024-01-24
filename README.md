# CallieShoeBot

## How to set up the bot, step by step

### 1) Download the bot file and required libraries

In order to host and run your own version of the CallieShoeBot, you must first download the main.py file located in this repository, or you can clone the whole repository. If you choose to clone this repository, I used [Poetry](https://python-poetry.org/) to handle dependencies, so you may have to set up your poetry install by regenerating the lock file (deleting and recreating it with `poetry lock`) and/or installing the dependencies (using `poetry install`), probably. Otherwise, you'll need to download the dependency [`discord-py-interactions`](https://pypi.org/project/discord-py-interactions/) through pip (`pip install discord-py-interactions`) or some other virtual environment setup, however you have it set up. *You must be running Python 3.10 or above.*

### 2) Create a discord application

To actually create a bot and invite it to a server, you must first [create a Discord application](https://discord.com/developers/applications) by following these steps:
1. Go to https://discord.com/developers/applications
2. Log into your Discord account.
3. Click on the "New Application" button in the top right of the window.
4. After naming and optionally setting an icon for the application, you must next click on the "Bot" section on the sidebar. 
5. Copy the bot token, and set the environment variable `BOT_TOKEN` with the bot token value on your server host. You may also be able to hardcode the token into the script (replacing `bot = interactions.Client(token=os.environ.get('BOT_TOKEN'))` with `bot = interactions.Client(token="some gibberish bot token string")`) but if you're going to commit to this repository I highly suggest you do not.

With this done, you can move on to the next step.

### 3) Invite the bot

After completing the previous step, you must click on "OAuth2" on the sidebar, and then click on "URL Generator" in the dropdown. Here, you must click on the box labled "bot" that is located near the middle of the window. Next you must define the permissions that the bot will be allowed. Technically, the bot should only need the Read Messages/View Channels, Send Messages, Send Messages in Threads (if you plan to use the bot in a thread), and Use Slash Commands, though for simplicity's sake you could simply give it Administrator permissions. Then, at the bottom of the page, there will be a link that you can use to invite the bot to the server you intend to use it in, provided you have permissions to invite bots to said server.

### 4) Customizing and running the bot

At this point you can now add, remove, or alter the modifiers, chances of rolling modifiers, and blacklist weapons, subs, and the like. Modifiers are selected by choosing a random index within the list embedded in the `randomModifier`, thus some modifiers are listed twice in order to have boosted odds. Adding, removing, and making certain modifiers more likely can all be done by editing this list. If you are adding a modifier, make sure you add the associated modifier to `modifier_function`.

If you wish to alter the Double Down modifiers, then you will need to scroll to the `doubledown_function` function and edit the lists of modifiers there. Make sure the modifier you are adding is in `modifier_function`.

If you wish to alter the list of weapons, subs, or specials that can be selected, then you must edit the lists that can be found in the `randomWeapon`, `randomSub`, and `randomSpecial` functions. If you wish to alter the list of available maps or game modes that can be selected, then you must edit the lists that can be found in `maplist_function`. Altering the list of gear abilities goes into the `randomHeadgearAbility`, `randomClothingAbility`, or the `randomShoesAbility`, as needed. Editing any of these lists *does not* require you to edit the `modifier_function`.

After all of your desired changes have been made, you can simply run the main.py file in your desired IDE or hosting service and your bot should become online.

If you choose to clone this repository, you can also run the bot on your server by running `poetry run python main.py` in the main directory of the git repository.
