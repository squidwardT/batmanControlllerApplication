import sys
sys.path.append('..')
from run_command import run_command
from batman_socket import BatmanSocket
from BatmanServerSocket import BatmanServerSocket

class BatmanClientServerSocket(BatmanServerSocket):
	'''CLASS: Representing a BATMAN-Advanced node capable of listening, interpreting
	          actions, and transmitting data.

	FIELDS:
	@transmission_client		-- A socket capable of sending out data to other nodes.
	'''
	def __init__(self, address, client = None):
		super(BatmanClientServerSocket, self_.__init__(address)
		# Initialize transmission client
		if client is None:
			self.transmission_client = BatmanSocket()
		else:
			self.transmission_client = client

	def replace_client(self):
		'''Create new transmission client.'''
		self.transmission_client = BatmanSocket()

	def read_client(self, client, address):
		'''Get the arguments from the server socket and interpret them.

		ARGS:
		@client 		-- The client socket to read from.
		@address		-- The address of the client socket (for returning data)

		RETURNS:
		None
		'''

		args = BatmanServerSocket.read_client(client)
		self.interpret_args(args, client)

	def interpret_args(self, args, client, address):
		'''Interpret the arguments received from another device and do what they ask.

		ARGS:
		@args 			-- The list of arguments to execute.
		@client 		-- The client the data came from.
		@address		-- The client's return address.

		RETURNS:
		None
		'''
		if args[0] == 'ping':
			(stdout, stderr) = run_command('sudo batctl ping -c 1' + args[1])
			xml_ping = xml_parser.parse_ping_to_xml(stdout)
			client_send_message(address, 'ping_response ' + open(xml_ping, 'r').read())
		elif args[0] == 'traceroute':
			(stdout, stderrr) = run_command('sudo batctl traceroute ' + args[1])
			xml_traceroute = xml_parser.parse_traceroute_to_xml(stdout)
			client_send_message(address, 'traceroute_response ' + open(xml_traceroute, 'r').read())

	def client_send_message(self, host, message, port = 56634):
		'''Send a message.

		ARGS:
		@host			-- The host to send data to.
		@message 		-- The data to send
		@port 			-- The port the application is listening on.

		RETURNS:
		None
		'''
		self.transmission_client.connect(host, port)
		self.transmission_client.write(message)
		self.replace_client()
		


		 
