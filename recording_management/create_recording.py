def create_recording(duration, filename, el_format = 'wav'):
	'''Create a recording using the Raspberry Pi Sound Card.

	ARGS:
	@duration		-- The length of time to record.
	@filename		-- The name of the recording file
	@format 		-- The audio format to use.

	RETURN:
	None
	'''
	import time

	process = start_recording(filename, el_format)
	time.sleep(duration)
	stop_recording(process)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', 'duration')
	parser.add_argument('-f', 'filename')
	args = parser.parse_args()

	create_recording(args.duration, args.filename)

