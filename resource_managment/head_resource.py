def head_resource(uri):
	'''Get the metadata on a resource.

	ARGS:
	@uri		-- The uri for locating the resource in relation to the
				   resources directory. Ex networks/config.

	RETURNS:
	@metadata 	-- The metadata associated with the uri given.
	'''
	from find_resource import find_resource
	path = find_resource(uri)
	return the meta data when we figure out how this will be structured