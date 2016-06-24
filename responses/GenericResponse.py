from responses import BaseResponse

class GenericResponse(BaseResponse.ResponseBase):
	accept = []
	parent = None
	latestreceived = "notset"

	def receive_message(self, message):
		print(self.latestreceived)
		self.latestreceived = message['type'] 
		print(self.latestreceived)
