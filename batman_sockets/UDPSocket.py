import socket

def send_message(message, host, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(message, (host, port))
	chunks = []
	while True:
		chunk, address = sock.recvfrom(1028)
		if chunk == '':
			break
		chunks.append(chunk)
	return ''.join(chunks)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('m', 'message')
	parser.add_argument('h', 'host')
	parser.add_argument('p', 'port')

	send_message(args.message, args.host, args.port)