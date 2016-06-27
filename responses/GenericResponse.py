from responses import BaseResponse

class GenericResponse(BaseResponse.ResponseBase):
	accept = []
	socket = None
	slackinfo = None

	def receive_message(self, message):
		pass
