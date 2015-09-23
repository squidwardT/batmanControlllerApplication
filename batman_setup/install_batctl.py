from run_command import run_command

def install_batctl():
	'''Installs batctl a BATMAN-Advanced configuration tool.

	ARGS:
	None

	RETURN:
	None
	'''
	
	run_command('sudo apt-get batctl')

if __name__ == '__main__':
	install_batctl()