def display_menu():
	import sys
	sys.path.append('..')
	from interpret_command import interpret_command
	print 'MENU OPTIONS'
	print '1. Download and Install Batman'
	print '2. Configure Device on Network'
	print '3. Create Recording'
	print '4. Playback Recording'
	print '5. View Network Information'
	print '6. Get Resource from Server'
	print '7. Post Resource to Server'
	print '8. Create User'
	print '9. Login'
	print 'Please Enter the number of the option you would like to perform.'
	print 'Input: '
	command = raw_input()
	interpret_command(command)

if __name__ == '__main__':
	display_menu()