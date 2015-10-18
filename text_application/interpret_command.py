def interpret_command(command):
	import sys
	sys.path.append('..')
	if command == '1':
		from batman_setup import install_batman_raspbian
		install_batman_raspbian()
	elif command == '2':
		from network_management import join_batman_network_guest
		print 'ESSID: '
		essid = raw_input()
		print 'Access Point Mac Address: '
		ap = raw_input()
		print 'IP Range: '
		ip_range = raw_input()
		join_batman_network_guest(essid, ap, ip_range)
	elif command == '3':
		from recording_management import create_recording
		print 'Name: '
		name = raw_input()
		print 'Duration: '
		duration = raw_input()
		create_recording(duration, name)
	elif command == '4':
		from recording_management import play_recording
		print 'Name: '
		name = raw_input()
		play_recording(name)
	elif command == '5':
		###PLACEHOLDER###
	elif command == '6':
		from server_communication import get_resource_from_server
		print 'Resource Path: '
		path = raw_input()
		get_resource_from_server(path)
	elif command == '7':
		from server_communication import post_resource_to_server
		print 'Resource Path: '
		path = raw_input()
		print 'Data: '
		data = raw_input()
		post_resource_to_server(path, data)
	else:
		print 'The Command You Entered Was Invalid'

	terminate_app()
