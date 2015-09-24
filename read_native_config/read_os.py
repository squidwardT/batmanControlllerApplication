def read_os():
	'''Read the OS of the device.

	ARGS:
	None

	RETURNS:
	None
	'''
	from platform import system
	return system()

if __name__ == '__main__':
	print read_os()