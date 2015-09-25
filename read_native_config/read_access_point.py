def read_access_point(interface):
	'''Read the MAC address of the access point associated
	with the network that @interface is on.

	ARGS:
	@interface 		-- The interface inquired about.

	RETURNS:
	@ap 			-- The MAC address of the interface's
					   network access point.
	'''
	from parse_iwconfig import parse_iwconfig

	interfaces = parse_iwconfig()
	for intrfc in interfaces:
		if intrfc['interface'] == interface:
			return interface['ap']