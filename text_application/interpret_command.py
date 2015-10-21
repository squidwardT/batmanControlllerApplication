def interpret_command(command):
	import sys
	sys.path.append('..')
	if command == '1':
		from batman_setup.install_batman_raspbian import install_batman_raspbian
		install_batman_raspbian()
	elif command == '2':
		from network_management.join_batman_network_guest import join_batman_network_guest
		print 'ESSID: '
		essid = raw_input()
		print 'Access Point Mac Address: '
		ap = raw_input()
		print 'IP Range: '
		ip_range = raw_input()
		join_batman_network_guest(essid, ap, ip_range)
	elif command == '3':
		from recording_management.create_recording import create_recording
		print 'Name: '
		name = raw_input()
		print 'Duration: '
		duration = raw_input()
		create_recording(duration, name)
	elif command == '4':
		from recording_management.play_recording import play_recording
		print 'Name: '
		name = raw_input()
		play_recording(name)
	elif command == '5':
		###PLACEHOLDER###
		print 'This action is not supported yet'
	elif command == '6':
		from server_communication.get_resource_from_server import get_resource_from_server
		print 'Resource Path: '
		path = raw_input()
		get_resource_from_server(path)
	elif command == '7':
		from server_communication.post_resource_to_server import post_resource_to_server
		print 'Resource Path: '
		path = raw_input()
		print 'Data: '
		data = raw_input()
		post_resource_to_server(path, data)
	elif command == '8':
		from server_communication.post_resource_to_server import post_resource_to_server
		print 'Name: '
		name = raw_input()
		print 'Email: '
		email = raw_input()
		print 'Password: '
		pw = raw_input()
		print 'Password Confirmation: '
		pw_confirm = raw_input()
		data = { 'user' : { 'name' : name,
				 			'email': email,
				 			'password' : pw,
				 			'password_confirmation' : pw_confirm },
				 'commit' : 'Create my account' }
		post_resource_to_server('users', data)
	else:
		print 'The Command You Entered Was Invalid'

	from terminate_app import terminate_app
	terminate_app()
