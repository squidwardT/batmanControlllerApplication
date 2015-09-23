from run_command import run_command
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

	def read_client(self, client):
		args = BatmanServerSocket.read_client(client)
		self.interpret_args(args, client)

	def interpret_args(self, args, client):
		if args[0] == 'ping':
			(stdout, stderr) = run_command('sudo batctl ping ' + args[1])
		elif args[0] == 'traceroute':
			(stdout, stderrr) = run_command('sudo batctl tracerout ' + args[1])
		return stdout

	def client_send_message(host, message, port = 56634):
		self.transmission_client.connect(host, port)
		self.transmission_client.write(message)
		self.replace_client()
		


		 
