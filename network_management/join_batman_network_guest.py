def join_batman_network_guest(ssid, ap, ip_range):
	'''Join the Batman network in the guest IP spot.

	ARGS:
	@ssid		-- The name of the network to be joined.
	@ap 		-- The MAC address of the access point of the network.
	@ip_range 	-- The IP address range of the network being joined.

	RETURNS:
	None		-- Sends a message to the network access point with device address
				   information to which the access point should respond with a
				   switch IP message.
	'''
	import sys
	sys.path.append('..')
	from run_command import run_command
	from batman_sockets import BatmanClientServerSocket

	# If network information invalid do not change network settings just QUIT.
	if not is_valid_ip_range(ip_range) or not is_valid_mac_address(ap):
		return None

	# Determine gateway and guest IP address based on the IP range
	ip = ip_range + '.255'
	gateway_ip = ip_range + '.0'

	# Configure the BATMAN-Advanced network using the guest ip
	join_batman_network(ssid, ap, ip)

	# Create a socket with a port the device will listen for messages on and then send a
	# message to the access point with information about communicating with the device.
	# The access point should respond with a switch IP message.
	batman_socket = BatmanClientServerSocket.BatmanClientServerSocket(address)
	batman_socket.client_send_message(gateway_ip, 'hello ' + ip + ' ' + str(batman_socket.port))
