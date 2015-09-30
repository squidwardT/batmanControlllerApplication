import *

def interpret(command):
	response = None

	from shlex import split
	args = split(command)
	if args[0] == 'GET':
		response = get_resource(args[1])
	elif args[0] == 'POST':
		post_resource(args[1], args[2])
	elif args[0] == 'HEAD':
		response = head_resource(args[1])
	elif args[0] == 'PUT':
		put_resource(args[1], args[2])
	elif args[0] == 'DELETE':
		delete_resource(args[1])
	elif args[0] == 'TRACE':
		post_resource(args[1], args[2])
		reponse = args[2]
	elif args[0] == 'OPTIONS':
		options_resource(args[1])