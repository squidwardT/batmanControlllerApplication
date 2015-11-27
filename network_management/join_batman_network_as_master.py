def join_batman_network_as_master(ssid = 'squids_network',
								  ap = '02:12:34:56:78:9A',
								  channel = 1,
								  gateway = True):
	import sys
	import threading
	sys.path.append('..')
	from run_command import run_command

	if gateway:
		from join_batman_network_as_gateway import join_batman_network_as_gateway
		interface = 'br-lan'
		join_batman_network_as_gateway(ssid, ap, channel)
	else:
		from join_batman_network import join_batman_network
		interface = 'bat0'
		join_batman_network(ssid, ap, channel)

	with open('/etc/dhcp/dhcpd.conf', 'w') as dhcp_file:
		dhcp_file.write('ddns-update-style none;\n\n' +
						'default-lease-time 600;\n' +
						'max-lease-time 7200;\n\n' +
						'authoritative;\n\n' +
						'subnet 192.168.10.0 netmask 255.255.255.0 {\n' +
						'	range 192.168.10.10 192.168.10.250;\n' +
						'	option broadcast-address 192.168.10.255;\n' +
						'	option routers 192.168.10.1;\n' +
						'	default-lease-time 600;\n' +
						'	max-lease-time 7200;\n' +
						'	option domain-name "batlan";\n' +
						'	option domain-name-servers 8.8.8.8 8.8.4.4;\n' +
						'}')

	with open('/etc/default/isc-dhcp-server', 'w') as server_file:
		server_file.write('INTERFACES="' + interface + '"')

	run_command('sudo ifdown wlan0')
	with open('/etc/network/interfaces', 'w') as interfaces_file:
		interfaces_file.write('auto lo\n\n' +
							  'iface lo inet loopback\n' +
							  'iface eth0 inet dhcp\n\n' +
							  'allow-hotplug ' + interface + '\n\n' +
							  'iface ' + interface + ' inet static\n' +
							  ' address 192.168.10.1\n' +
							  ' netmask 255.255.255.0')

	command = 'sudo service isc-dhcp-server restart'
	thread = threading.Thread(target=run_command, args=(command, ))
