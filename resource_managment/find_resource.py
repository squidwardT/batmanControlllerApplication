def find_resource(uri):
	'''Find and return a resources path.

	ARGS:
	@uri 		-- The uri for locating the resource in relation to the
				   resources directory. Ex networks/config.

	RETURNS:
	@path		-- Full path of the uri.
	'''
	import os
	from string import split
	return os.path.join(os.path.abspath(__file__), '../resources', 
		                split(uri, '/'))