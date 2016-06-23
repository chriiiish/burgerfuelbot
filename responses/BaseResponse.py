class ResponseBase:
	# The type of messages received from Slack (e.g. 'hello', 'message', 'user_typing'). If empty list then all messages will be sent 
	accept = []
	parent = None

	# Constructor - Passed in parent (used to send things back to slack
	def __init__(self, parent):
		self.parent = parent

	# This is called when any message (that has been specified by accept) has been received.
	def receive_message(self, message):
		pass

	# Sends things back to slack
	def send_message(self, message):
		self.parent.send(message)
	
		
