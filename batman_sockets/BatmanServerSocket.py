import shlex
import select
import socket
from threading import Thread
from BatmanSocket import BatmanSocket

class BatmanServerSocket(BatmanSocket):

	'''CLASS: Representing a BATMAN-Advanced node as a server socket listening on
			  a port to take action or pass data

	FIELDS:
	@self.socket 	-- The child socket this socket has been built from.
	@self.clients	-- The list of clients that are communicating with this device in
					   some way
	'''

	def __init__(self):
		'''CONSTRUCTOR: Run parent constructor and initialize the clients array'''
		super(BatmanServerSocket, self).__init__(self)
		self.clients = []

	def start_server(self, port):
		'''Listen on a @port for incoming application connections. When connected to
		store the client's information and attempt to read its transmitted data.

		ARGS:
		@port		-- The port number to start the server socket on

		RETURN:
		None		-- Theoretically Endless
		'''

		self.sock.bind((socket.gethostname(), port))
		self.sock.listen(5)

		while True:
			client, address = self.sock.accept()
			batman_client = BatmanSocket(address, client, address)

			add_thread = Thread(target = self.add_client, args = [batman_client])
			read_thread = Thread(target = self.read_client, args = [batman_client])
			add_thread.start()
			read_thread.start()

	def update_client(self, client):
		ready_to_read, ready_to_write, in_error = select.select(self.clients,
												  self.clients, self.clients, 60.0)
		for item in in_error:
			self.clients.remove(item)

		for item in ready_to_read:
			self.read_client(item)

		for item in self.clients:
			if item.address == client.address:
				self.clients.remove(user)


	def add_client(self, clients):
		'''Add a client '''

		client = clients
		self.update_client(client)
		self.clients.append(client)
			

	def read_client(self, clients, address = None):
		client = clients
		message = client.read()
		args = shlex.split(message)

		out = []
		if 'g' in args[0]:
			for arg in args[1 : ]:
				response = client.get(arg)
				out.append(response)
		if 'p' in args[0]:
			for arg in args[1 : ]:
				client.post(arg)
		if 'd' in args[0]:
			for arg in args[1 : ]:
				client.display(arg)

if __name__ == '__main__':
	server = BatmanServerSocket()
	server.start_server(56634)

