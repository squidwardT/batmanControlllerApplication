def read_ip_mac_tuple(interface):
	'''Read an interfaces IP and MAC address.

	ARGS:
	@interface 			-- The interfaces IP and MAC to be read. Ex. Bat0, Eth0

	RETURNS:
	@ip 				-- The interfaces IP as a STRING.
	@mac 				-- The interfaces MAC as a STRING.
	'''
	from read_ip_address import read_ip_address
	from read_mac_address import read_mac_address
	ip = read_ip_address(interface)
	mac = read_mac_address(interface)

	return (ip, mac)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('interface')
	args = parser.parse_args()

	ip, mac = read_ip_mac_tuple(args.interface)
	print ip 
	print mac