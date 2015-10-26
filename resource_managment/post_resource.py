def post_resource(uri, data):
    '''Post a resource to this @uri.

    ARGS:
    @uri		-- The uri for locating the resource in relation to the
                               resources directory. Ex networks/config.

    RETURNS:
    None
    '''
    from find_resource import find_resource
    path = find_resource(uri)
    with open(path, 'w') as resource:
        resource.write(data)
