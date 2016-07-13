from responses import BaseResponse

class HelloResponse(BaseResponse.ResponseBase):
	accept = []
	socket = None
	slackinfo = None
	hello = ["hi","yo", "whats up", "what's up", "hello", "sup"]

	def receive_message(self, message):
		if message['type'] == "message":
			self.process_message(message)
	
	# Handles Messages
	def process_message(self, message):
		if ("<@%s>" % self.slackinfo['self']['id']) in message['text'] and self.keyword_match(message['text'].lower(), self.hello):
			self.send_message("Hi <@%s>" % message['user'], message['channel'])
			print("Responding to %s" % message['user']) 
