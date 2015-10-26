def delete_resource(uri):
	'''Delete a resource.

	ARGS:
	@uri		-- The uri for locating the resource in relation to the
				   resources directory. Ex networks/config.

	RETURNS:
	None
	'''
	import os
	from find_resource import find_resource
	path = find_resource(uri)
	os.remove(path)