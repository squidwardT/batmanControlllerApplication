from batman_socket import BatmanSocket
from BatmanServerSocket import BatmanServerSocket

class BatmanClientServerSocket(BatmanServerSocket):
	def __init__(self, address, client = None):
		super(BatmanClientServerSocket, self_.__init__('idc')
		if client is None:
			self.transmission_client = BatmanSocket()
		else:
			self.transmission_client = client

	def replace_client(self):
		self.transmission_client = BatmanSocket()

	def read_client(self, clients):
		args = BatmanServerSocket.read_client(clients)
		interpreter = Interpreter(self)
		interpreter.interpret(args)

	def client_send_message(host, message, port = 56634):
		self.transmission_client.connect(host, port)
		self.transmission_client.write(message)
		self.replace_client()
		


		 
