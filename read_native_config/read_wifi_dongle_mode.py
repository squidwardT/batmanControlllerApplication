def read_wifi_dongle_mode(interface):
	'''Read the mode of a Wireless device's interface.

	ARGS:
	@interface 		-- The name of the interface inquired about.

	RETURNS:
	@mode 			-- The mode of the Wireless device. Ex Mangaged
	'''
	from parse_iwconfig import parse_iwconfig

	interface = parse_iwconfig()
	for intrfc in interfaces:
		if intrfc['interface'] == interface:
			return interface['mode']