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
	from BeautifulSoup import BeautifulSoup

	# Build the path to the resource
	abs_path = 'http://batphone.co:3000/' + rsc_path
	print 'Posting to ' + abs_path

	# GET an authenticity token 
	session = requests.Session()
	html = BeautifulSoup(session.get('http://batphone.co:3000/login').text)
	csrf = html.head.find('meta', attrs = {'name' : 'csrf-token'})['content']
	payload['authenticity_token'] = csrf

	# Define a JSON header
	header = {'content-type' : 'application/json'}
	
	# Post data in JSON format with the JSON header
	response = session.post(abs_path, 
		 					headers = header, 
		 					data = json.dumps(payload))

	# Check whether the POST was successful
	if session.status_code == 200:
		print 'Success'
		return session
	else: print str(session.status_code)
	return False

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	parser.add_argument('payload')
	args = parser.parse_args()

	path = 'users'
	data = {'user' : {'name' : 'squid',
			'email': 'sqt@hotmail.com',
			'password' : 'helloworld',
			'password_confirmation' : 'helloworld'},
			'commit' : 'Create my account'}
	post_resource_to_server(args.path, args.payload)
