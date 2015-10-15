def play_recording(name, interface = 'headset'):
	import sys
	sys.path.append('..')
	from run_command import run_command

	if interface == 'headset':
		run_command('./Playback_to_Headset.sh')

	command = 'aplay ' + filename
	run_command(command)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('name')
	args = parser.parse_args()

	play_recording(args.name)