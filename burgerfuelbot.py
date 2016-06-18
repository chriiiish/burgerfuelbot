from websocket import create_connection
import urllib.request
import json
import sys

# Check to make sure we're in Python 3!
if ( sys.version_info < (3,0) ):
	print("You must be using Python 3!")
	exit()


# Setup URLs
urls = {
		"auth" : "https://slack.com/api/rtm.start",
		"socket" : "",
}

# Slack Access Token (https://api.slack.com/bot-users)
token = ""	


# Get the websocket URL
print("Connecting to Slack...")
response = ""
url = "%s?token=%s" % (urls['auth'], token)
with urllib.request.urlopen( url ) as req:
	response = req.read()

slackinfo = json.loads( (response.decode('utf-8')) )

# Check that the response has been received
if ( not slackinfo['ok'] ):
	print("Request to Slack Failed.")
	print("Error: %s" % slackinfo['error'])
	exit()
else:
	print("Connection to Slack Successful")

# Store the important things from slack info object
urls['socket'] = slackinfo['url']

# Open the websocket to slack
print("Opening connection to Slack Websocket Engine...")
socket = create_connection(urls['socket'])

run = True

print("Monitoring...")
try:
	while run:
		result = socket.recv()
		jsonresult = json.loads(result)
		print("Received %s" % str(jsonresult['type']))
except KeyboardInterrupt as interrupt:
	print("")
	print("Stopping Server...")

socket.close()
