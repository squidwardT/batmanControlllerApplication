def get_resource(uri):
	'''Open the resource, read and return its data.

	ARGS:
	@uri 		-- The uri for locating the resource in relation to the
				   resources directory. Ex networks/config.

	RETURNS:
	@data 		-- The data contained in the file as a String.
	'''
	from find_resource import find_resource

	path = find_resource(uri)
	with open(path, 'r') as resource:
		return resource.read()
