def read_os():
	from platform import system
	return system()

if __name__ == '__main__':
	print read_os()