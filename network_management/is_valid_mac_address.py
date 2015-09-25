def is_valid_mac_address(mac):
	import re
	mac_pattern = '^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$'
	if re.search(mac_pattern, mac) is not None:
		return True
	return False

if __name__ == '__main__':
	print str(is_valid_mac_address('00:00:00:00:00:00'))