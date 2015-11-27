def setup(ssid, publickey, dev_name, IP_address, MAC, Gateway_mode, 
	      description, location, notes):
	import sys
	sys.path.append('..')
	from string import split
	from server_communication import post_resource_to_server

	net_info = { 'name' : ssid,
				 'publickey' : publickey }
	network_payload = { 'network' : net_info,
						'commit' : 'Add Network'}
	session, response = post_resource_to_server.post_resource_to_server('networks', network_payload)
	network_id = split(response.url, '/')[-1]

	dev_info = { 'name' : dev_name,
				 'IP_address' : IP_address,
				 'MAC' : MAC,
				 'AP_SSID' : ssid,
				 'Gateway_mode' : Gateway_mode,
				 'description' : description,
				 'location' : location,
				 'notes' : notes }
	device_payload = { 'device' : dev_info,
					   'network_id' : network_id,
					   'commit' : 'Add Device' }
	session, repsonse = post_resource_to_server.post_resource_to_server('devices', device_payload, session)

if __name__ == '__main__':
	setup('roxbury', 'hill', 'mine', '66.66.56.66', '11:22:33:DD:EE:FF', 
		  'server', '-#-#-', 'the palace', 'what?')