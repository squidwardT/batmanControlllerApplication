def join_batman_network_as_client(ssid = 'squids_network',
								  ap = '02:12:34:56:78:9A',
								  channel = 1,
								  gateway = False):
	import sys
	sys.path.append('..')
	from run_command import run_command
	
	if gateway:
		(from join_batman_network_as_gateway 
		 import join_batman_network_as_gateway)
		join_batman_network_as_gateway(ssid, ap, channel)
	else:
		from join_batman_network import join_batman_network
		join_batman_network(ssid, ap, channel)