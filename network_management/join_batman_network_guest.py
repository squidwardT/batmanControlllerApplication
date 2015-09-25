def join_batman_network_guest(ssid, ap, ip_range):
	import sys
	sys.path.append('..')
	from run_command import run_command
	from batman_sockets import BatmanClientServerSocket

	if not is_valid_ip_range(ip_range) or not is_valid_mac_address(ap):
		return None

	ip = ip_range + '.255'
	gateway_ip = ip_range + '.0'
	join_batman_network(ssid, ap, ip)
	batman_socket = BatmanClientServerSocket.BatmanClientServerSocket(address)
	batman_socket.client_send_message(gateway_ip, 'hello ' + ip + ' ' + str(batman_socket.port))
