def join_batman_network_as_gateway(ssid, ap, channel):
	'''Join the Batman network as a gateway node.

	ARGS:
	@ssid		-- The name of the network to be joined.
	@ap 		-- The MAC address of the access point of the network.
	@ip_range 	-- The IP address range of the network being joined.

	RETURNS:
	None		
	'''
	import sys
	sys.append.path('..')
	from run_command import run_command

	run_command('sudo ip link set mtu 1532 wlan0')
	run_command('sudo ifconfig wlan0 down ' +
	 			'&& sudo iwconfig wlan0 mode ad-hoc essid ' + 
	 			ssid + 
	 			' ap ' +
	 			ap  +
	 			' channel ' + 
	 			str(channel))
	run_command('sudo batctl if add wlan0')
	run_command('sudo ip link set up dev wlan0')
	run_command('sudo ip link add name br-lan type bridge')
	run_command('sudo ip link set dev eth0 master br-lan')
	run_command('sudo ip link set dev bat0 master br-lan')
	run_command('sudo ip link set up dev eth0')
	run_command('sudo ip link set up dev bat0')
	run_command('sudo ip link set up dev br-lan')
	run_command('sudo batctl gw_mode server')

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('ssid')
	parser.add_argument('ap')
	parser.add_argument('ip_range')
	args = parser.parse_args()

	join_batman_network_as_gateway(args.ssid, args.ap, args.ip_range)

	
