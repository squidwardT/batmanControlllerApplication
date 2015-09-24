def read_ip_address(interface):
	import netifaces
	if interface not in netifaces.interfaces():
		return None

	return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('interface')
	args = parser.parse_args()

	print read_ip_address(args.interface)
