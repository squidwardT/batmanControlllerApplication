def play_recording(name, interface = 'headset'):
	'''Playback a recording.

	ARGS:
	@name 		-- The file name of the recording.
	@interface 	-- The interface to play it over.

	RETURNS:
	None
	'''
	import os
	import sys
	sys.path.append('..')
	from run_command import run_command

	path = os.path.join(os.path.abspath(__file__), 
		                '../../resources/recordings', filename)

	if interface == 'headset':
		run_command('./Playback_to_Headset.sh')

	command = 'aplay ' + path
	run_command(command)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('name')
	args = parser.parse_args()

	play_recording(args.name)