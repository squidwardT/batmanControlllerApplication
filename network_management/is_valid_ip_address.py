def is_valid_ip_address(ip):
	import re

	ip_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)' +
				 '{3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
	if re.search(ip_pattern, ip) is not None:
		return True
	return False
