from responses import BaseResponse

class GenericResponse(BaseResponse.ResponseBase):
	accept = []
	parent = None

	def receive_message(self, message):
		print(message)
