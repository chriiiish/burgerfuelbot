**Disclaimer - This doesn't work yet ;P**
#burgerfuelbot#
Initially intended as a bot to manage our Burgerfuel eating habits this is a bot designed to connect to [Slack](https://slack.com/) and should be generic enough to handle all sorts of applications. Just because we use it for Burgerfuel doesn't mean you can't use it for anything else ;)


**Dependencies**
Uses [websocket-client](https://pypi.python.org/pypi/websocket-client): pip install websocket-client

Uses Python3!


----------
###Getting Started###
Once you've setup your Slack bot (see [here for information](https://api.slack.com/bot-users) and [here to create one](https://my.slack.com/services/new/bot)) and you've got your API token (e.g. xxxx-00000000000-xxxxxxxxxxxxxxxxxxxxxxxx) go into burgerfuelbot.py.


Inside that file you'll find a line near the top that says `token = "<your token here>"`. Chuck your token in there.


Once you've saved that - start up the server with `python3 burgerfuelbot.py`.


You should see some output along the lines of:
`Connecting to Slack...
Connection to Slack Successful
Opening connection to Slack Websocket Engine...
Monitoring...`


That means you're running!

**To stop the bot, use Ctrl+C**


----------

###A bit of debugging###

**Problem:** I get a message saying "`FileNotFoundError: [Errno 2] No such file or directory: './responses'`"
**Solution:** This means that you're not running burgerfuelbot.py from the burgerfuelbot directory. (Basically run python in the same directory that burgerfuelbot.py is located in). If you're doing anything like `python3 [somedirectory]\burgerfuelbot.py` it won't work.


**Problem:** I get a message saying `urllib.error.HTTPError: HTTP Error 400: BAD_REQUEST` after starting the bot.
**Solution:** This means (generally) that you haven't entered the token in burgerfuelbot.py. Eventually I'm hoping to put this into a config file so you won't need to worry about this, but it probably won't happen for a while.


