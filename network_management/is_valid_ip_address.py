def is_valid_ip_address(ip):
	'''Check a received IP address to make sure it fits 
	the IPv4 standard.

	ARGS:
	@ip 		-- The address to be examined.

	RETURNS:
	Boolean
	'''
	import re

	# Analyze the IP address based on the IPv4 standard
	# format (4 sequence dotted decimal number with a 
	# max value of 255 and minimum of 0)
	ip_pattern = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.)' +
				 '{3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
	if re.search(ip_pattern, ip) is not None:
		return True
	return False
