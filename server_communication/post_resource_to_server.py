def post_resource_to_server(rsc_path, payload):
	'''POST something to the server.

	ARGS:
	@rsc_path 		-- The path from the root of the application to the
					   resource to post.
	@payload 		-- The data to write to the resource.

	RETURNS:
	@request 		-- If the data was not received it is False, otherwise it
	 				   is the request object returned by the post.
	'''
	import json
	import requests

	# Build the path to the resource
	abs_path = 'http://batphone.co:3000/' + rsc_path

	# POST the data
	request = requests.post(abs_path, data=json.dumps(payload))
	
	# Check whether the POST was successful
	if request.status_code == '200':
		return request
	return False

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	parser.add_argument('payload')
	args = parser.parse_args()

	post_resource_to_server(args.path, args.payload)