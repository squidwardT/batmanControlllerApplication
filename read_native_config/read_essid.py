def read_essid(interface):
	'''Read the name of the network a Wireless device is 
	attached to.

	ARGS:
	@interface 		-- The interface inquired about. Ex wlan0

	RETURNS:
	@essid 			-- The name of the wireless network the device
					   is configured on.
	'''
	from parse_iwconfig import parse_iwconfig

	interfaces = parse_iwconfig()
	for intrfc in interfaces:
		if intrfc['interface'] == interface:
			return interface['essid']

