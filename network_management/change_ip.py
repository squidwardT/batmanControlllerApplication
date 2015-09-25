def change_ip(interface, ip):
	'''Change an interfaces IP address.

	ARGS:
	@interface  		-- The interface to be changed.
	@ip 				-- The new IP address to use.

	RETURNS:
	None
	'''
	import sys
	sys.path.append(..)
	from run_command import run_command

	run_command('sudo ifconfig ' + interface + ' ' + ip)