def start_recording(filename, el_format = '.wav'):
	'''Start a recording and leave it recording.

	ARGS:
	@filename 		-- The name of the recording to create.
	@el_format 		-- The format of the recording to create.

	RETURNS:
	@process 		-- The running process.
	'''
	import sys
	import shlex
	sys.path.append('..')
	from run_command import run_command
	from subprocess import Popen, PIPE

	run_command('./Record_from_DMIC.sh')

	command = ('arecord -Dhw:sndrpiwsp -r 44100 -c 2 -f S16_LE ' + filename 
	          + '.' + el_format)
	args = shlex.split(command)

	return Popen(args, stdout = PIPE, stderr = PIPE, shell = True)