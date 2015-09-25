def parse_iwconfig():
	'''Parser the iwconfig commands output into a list of
	dictionaries containing information about each wireless
	interface.

	ARGS:
	None

	RETURNS:
	@interfaces -- Interfaces as a LIST of DICTIONARIES 
				   Keys:
					  interface Ex. wlan0 				STRING
					  essid 	Ex. NUwave 				STRING
					  ap 		Ex. 02:12:34:56:78:9A   STRING
					  mode 		Ex. Managed, Ad-Hoc 	STRING
	'''

	import sys
	import shlex
	sys.path.append('..')
	from run_command import run_command

	# Run iwconfig and split stdout into interface chunks
	(stdout, stderr) = run_command('iwconfig')
	interfaces = stdout.split('\n\n')

	library = []
	for intrfc in interfaces:
		# Create a dictionary for each interface
		dictionary = {'interface' : None, 'essid' : None, 'ap' : None, 'mode' : None}
		essid_index = intrfc.find('ESSID:')
		mode_index = intrfc.find('Mode:')
		ap_index = intrfc.find('Access Point:')

		# If the interface isn't blank record it's info
		if len(shlex.split(intrfc)) > 0:
			# Grab the name of the interface and store it
			dictionary['interface'] = shlex.split(intrfc)[0]

			# Check that all other attributes exist and grab the ones
			# that do to be recorded
			if essid_index != -1:
				net = shlex.split(intrfc[essid_index + 6 :])[0]
				dictionary['essid'] = net
			if mode_index != -1:
				dongle_mode = shlex.split(intrfc[mode_index + 5 : ])[0]
				dictionary['mode'] = dongle_mode
			if ap_index != -1:
				mac = shlex.split(intrfc[ap_index + 13 : ])[0]
				dictionary['ap'] = mac

			# Append the interfaces dictionary to the list of them
			library.append(dictionary)
	return library

if __name__ == '__main__':
	lib = parse_iwconfig()
	for item in lib:
		print str(item)

