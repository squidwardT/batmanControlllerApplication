def write_networking_info(port):
	'''Grab BATMAN networking configuration and write them to a file to be
	published via the REST application.

	ARGS:
	@port		-- The number of the port that the device will be listening
				   for connections on

	RETURNS:
	REST INFO
	'''

	import os
	import sys
	sys.path.append('../read_native_config')
	from read_os import read_os
	from read_ip_mac_tuple import read_ip_mac_tuple

	os = read_os()
	(ip, mac) = read_ip_mac_tuple('wlan0')

	path = os.path.join(os.path.dirname(__file__), '../networks_config.txt')
	with open(path, 'w') as net_file:
		net_file.write('os : ' + os + '\n')
		net_file.write('ip : ' + ip + '\n')
		net_file.write('mac : ' + mac + '\n')
		net_file.write('port : ' + str(port) + '\n')
		net_file.flush()
		net_file.close()

if __name__ == '__main__':
	write_networking_info('80')




