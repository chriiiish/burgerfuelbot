import json

class ResponseBase:
	# The type of messages received from Slack (e.g. 'hello', 'message', 'user_typing'). If empty list then all messages will be sent 
	accept = []
	socket = None
	slackinfo = None
	latestpacketid = 1

	# Constructor - 
	def __init__(self, socket, slackinfo):
		self.socket = socket
		self.slackinfo = slackinfo

	# This is called when any message (that has been specified by accept) has been received.
	def receive_message(self, message):
		pass

	# Sends things back to slack
	def send_message(self, message, channel):
		ResponseBase.latestpacketid += 1
		self.socket.send(json.dumps({
    		"id": ResponseBase.latestpacketid - 1,
    		"type": "message",
    		"channel": channel,
    		"text": message
		}))	
