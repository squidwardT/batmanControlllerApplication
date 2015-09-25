def is_valid_mac_address(mac):
	'''Examines a received MAC address to make sure
	it fits the standard MAC address format.

	ARGS:
	@mac 		-- The address to be examined.

	RETURNS:
	Boolean
	'''
	# Examine an address using the MAC standard format 
	# (6 sequence 2 digit string separated by colons or dashes)
	import re
	mac_pattern = '^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$'
	if re.search(mac_pattern, mac) is not None:
		return True
	return False

if __name__ == '__main__':
	print str(is_valid_mac_address('00:00:00:00:00:00'))