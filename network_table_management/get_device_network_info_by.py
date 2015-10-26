def get_device_network_info_by(key, value):
	import sys
	import json
	sys.path.append('..')
	from resource_management.get_resource import get_resource

	string_data = get_resource('network_table.txt')
	data = json.loads(string_data)
	for device in data['devices']:
		if device[key] == value:
			return device
