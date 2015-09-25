def is_valid_ip_range(ip_range):
	'''Similarly to is_valid_ip_address this function checks
	that a @ip_range is a valid ip address missing the last
	dot and sequence in the IPv4 standard format

	ARGS:
	@ip_range 		-- The dotted decimal number to be examined.

	RETURNS:
	Boolean
	'''
	return is_valid_ip_address(ip_range + '.0')
