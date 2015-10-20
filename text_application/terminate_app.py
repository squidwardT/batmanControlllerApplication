def terminate_app():

	print 'Are you done? (y/n)'
	choice = raw_input()
	if choice.lower() == 'n':
		from display_menu import display_menu
		display_menu()
