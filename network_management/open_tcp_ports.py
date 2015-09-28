def open_tcp_ports():
	'''Find all open TCP ports above port 1000 on this machine.

	ARGS:
	None

	RETURNS:
	@ports 		-- The LIST of open tcp port INTEGERS
	'''

	import re
	import sys
	import string
	sys.path.append('..')
	from run_command import run_command

	stdout, stderr = run_command('netstat -l')
	print stdout
	ports = string.split(stdout, '\n')[2 : ]
	open_ports = []
	for port in ports:
		attributes = string.split(port)
		if attributes[5] != 'LISTEN' and attribues[4] != '*:*':
			continue

		port_num = port[3][2 : ]
		if not port_num.isdigit():
			continue

		open_ports.append(port_num)

	return open_ports

if __name__ == '__main__':
	ports = open_tcp_ports()
	for port in ports:
		print port


