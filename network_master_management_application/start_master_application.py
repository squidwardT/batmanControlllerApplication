def start_master_application(essid, ap, password):
    '''Start the master application on the network that you specify.

    ARGS:
    @essid 		-- the name of the network to put it on.
    @ap 		-- the mac address of the ap.

    RETURNS:
    None
    '''
    from batman_sockets.TCPServerSocket import TCPServerSocket
    from network_management.join_batman_network import join_batman_network
    from web_app_communication.create_app_network import create_app_network

    print 'Starting Network Master Application'

    ip = '168.192.2.1'
    try:
        session = create_app_network(essid, password, ap, ip)
    except:
        print('Could Not Connect To The Internet.\n' +
              'The network will be started in Isolation mode.\n' +
              'Note: The network will be changed to Universal mode if the ' +
              'master or any subservient node gains internet access.')

    join_batman_network(essid, ap, ip)
    socket = TCPServerSocket('168.192.2.1')
    socket.start_server()
