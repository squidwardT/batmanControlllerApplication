def interpret_command(command):
	import sys
	sys.path.append('..')
	if command == '1':
		from batman_setup.install_batman_raspbian import install_batman_raspbian
		install_batman_raspbian()
	elif command == '2':
		from network_management.join_batman_network_guest import join_batman_network_guest
		args = get_args_as_dict({'ESSID': None, 'MAC': None, 'IP Range': None})
		join_batman_network_guest(args['ESSID'], args['MAC'], args['IP Range'])
	elif command == '3':
		from recording_management.create_recording import create_recording
		args = get_args_as_dict({'Name': None, 'Duration': None})
		create_recording(args['Duration'], args['Name'])
	elif command == '4':
		from recording_management.play_recording import play_recording
		args = get_args_as_dict({'Name': None})
		play_recording(args['Name'])
	elif command == '5':
		###PLACEHOLDER###
		print 'This action is not supported yet'
	elif command == '6':
		from server_communication.get_resource_from_server import get_resource_from_server
		args = get_args_as_dict({'URI': None})
		get_resource_from_server(args['URI'])
	elif command == '7':
		from server_communication.post_resource_to_server import post_resource_to_server
		args = get_args_as_dict({'URI': None, 'Data': None})
		post_resource_to_server(args['URI'], args['Data'])
	elif command == '8':
		from server_communication.post_resource_to_server import post_resource_to_server
		args = get_args_as_dict({'name': None,
								 'email': None,
								 'password': None,
								 'password_confirmation': None})
		data = { 'user': args,
				 'commit' : 'Create my account' }
		post_resource_to_server('users', data)
	elif command == '9':
		from server_communication.post_resource_to_server import post_resource_to_server
	else:
		print 'The Command You Entered Was Invalid'

	from terminate_app import terminate_app
	terminate_app()

def get_args_as_dict(the_dict):
	for key in the_dict:
		print key + ':'
		the_dict[key] = raw_input()
	return the_dict
