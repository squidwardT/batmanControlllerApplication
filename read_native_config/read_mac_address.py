def read_mac_address(interface):
	import netifaces
	if interface not in netifaces.interfaces():
		return None

	return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('interface')
	args = parser.parse_args()

	print read_mac_address(args.interface)