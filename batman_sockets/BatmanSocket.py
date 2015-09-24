import socket

class BatmanSocket(object):

	def __init__(self, address, sock = None):
		self.address = address

		if sock is None:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock

	def create_socket(self):
		self.sock = socket.socket(socket.socket.AF_INET, socket.SOCK_STREAM)

	def connect(self, host, port):
		self.sock.connect((host, port))

	def write(self, message):
		total = 0
		while total < len(message):
			sent = self.sock.send(message[total:])
			if sent == 0:
				raise RuntimeError('Connection Broken')
			total = total + sent

	def read(self):
		chunks = []
		total_recieved = 0
		while total_recieved < 7:
			chunk = self.sock.recv(min(7 - total_recieved, 2048))
			if chunk == '':
				raise RuntimeError('Connection Broken')
			chunks.append(chunk)
			total_recieved = total_recieved + len(chunk)
		return ''.join(chunks)

	def display(self, message):
		print message + '\n'

if __name__ == '__main__':
	socket = BatmanSocket('hello')
	socket.connect('129.10.33.161', 56634)
	socket.write('d hello')
