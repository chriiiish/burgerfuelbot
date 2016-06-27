from responses import BaseResponse

class EchoResponse(BaseResponse.ResponseBase):
	accept = []
	socket = None
	slackinfo = None

	def receive_message(self, message):
		if message['type'] == "message":
			self.process_message(message)
	
	# Handles Messages
	def process_message(self, message):
		if ("<@%s>" % self.slackinfo['self']['id']) in message['text']:
			self.send_message("Hi <@%s>" % message['user'], message['channel'])
			print("Responding to %s" % message['user']) 
