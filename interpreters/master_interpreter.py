class MasterInterpreter():

    '''An Argument Interpreter meant to control the way a network master
       interacts with its slave devices.

       For now there are only two methods GET and HELLO.

       GET is used by slave devices to collect network information from the
       master overwriting the older versions of resources and adding the new
       information on the slave device.

       The response from a GET is a POST request to the slave of the
       resource it requested.

       HELLO is used to announce a devices appearance on the network. It
       tells the master that it is on the network and the address it's
       listening on along with other network information such as mac address,
        tcp port, and udp port.

       The response from a HELLO is a SWITCH request to the slave asking it to
       change its IP address.
    '''
    def interpret(command):
        '''Any command received should be handled here or is invalid. This
           function allows a command received by a master device to be parsed,
           interpreted, and executed as expected. This gives slave devices a
           language to allow them to communicate with master devices in such a
           way that they can update the master of network information and grab
           resources from the master.

        ARGS:
        STRING @command 	-- the command to be executed by the master.

        RETURNS:
        STRING @response 	-- the response command to the command passed.
        '''
        import sys
        import json
        import shlex
        sys.path.append('..')

        # Split it
        args = shlex.split(command)
        try:
            # Check the first argument for the command
            if args[0] == 'BATGET':
                # If it is a get grab the resource using the path and POST it
                # on the slave device at the same location.
                from resource_management.get_resource import get_resource
                return get_resource(args[1])
            elif args[0] == 'BATPOST':
                # Make sure there is data and place to put it attached
                if args[1] is not None and args[2] is not None:
                    from resource_management.post_resource import post_resource

                    # If a something else tells the master to change its network
                    # information REJECT their request.
                    if args[1] == 'batnet_attrs.txt':
                        return '500 Master Devices cannot change network'
                    post_resource(args[1], json.loads(args[2]))
                    return '200'
            elif args[0] == 'SERVPOST':
                # POST to server if there is data and a place to POST it
                # This option is for slaves to PASS information to the server
                if args[1] is not None and args[2] is not None:
                    (from server_communication.post_resource_to_server 
                     import post_resource_to_server)

                    # This will return an instance from the requests module
                    # NEED TO DECIDE WHAT INFORMATION I SHOULD RESPOND TO
                    # SERVGET AND SERVPOST WILL BE
                    post_resource_to_server(args[1], args[2])

            elif args[0] == 'SERVGET':
                # GET from the server and respond to client with information
                if args[1] is not None:
                    (from server_communication.get_resource_from_server
                      import get_resource_from_server)

                    # This will return an instance from the requests module
                    # NEED TO DECIDE WHAT INFORMATION I SHOULD RESPOND TO
                    # SERVGET AND SERVPOST WILL BE
                    return get_resource_from_server(args[1])
        except:
            propogate(args)