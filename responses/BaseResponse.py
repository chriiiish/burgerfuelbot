class ResponseBase:
	# The type of messages received from Slack (e.g. 'hello', 'message', 'user_typing'). If empty list then all messages will be sent 
	accept = []
	parent = None

	# Constructor - 
	def __init__(self):
		#self.parent = parent
		pass

	# This is called when any message (that has been specified by accept) has been received.
	def receive_message(self, message):
		pass

	# Sends things back to slack
	def send_message(self, message):
		pass	
		
