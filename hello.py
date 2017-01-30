def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    # print(environ)
    # return environ[0]
return ["\n".join(environ["QUERY_STRING"].split("&"))]
