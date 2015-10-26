def start_master_application(essid, ap):
	'''Start the master application on the network that you specify.
	
	ARGS:
	@essid 		-- the name of the network to put it on.
	@ap 		-- the mac address of the ap.

	RETURNS:
	None
	'''
	from batman_sockets.TCPServerSocket import TCPServerSocket
	from network_management.join_batman_network import join_batman_network

	print 'Starting Network Master Application'
	join_batman_network(essid, ap, '168.192.2.1')
	socket = TCPServerSocket('168.192.2.1')
	socket.start_server()

