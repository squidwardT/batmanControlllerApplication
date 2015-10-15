def stop_recording(process):
	'''Terminate and kill a given process.

	ARGS:
	@process 		-- The recording process to stop.

	RETURN:
	None
	'''
	process.terminate()
	process.kill()