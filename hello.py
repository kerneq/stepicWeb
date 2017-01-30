from urllib.parse import urlparse, parse_qs

def app(environ, start_response):
    o = parse_qs(urlparse("?" + str(environ.get('QUERY_STRING', ''))).query, keep_blank_values=True)
    response = b''
    
    for key in list(sorted(o.keys())):
	   	response += bytes(str(key), encoding = 'utf-8') + bytes(str("="), encoding = 'utf-8') + \
 		bytes(str(o[key][0]), encoding = 'utf-8') + bytes(str("\n"), encoding = 'utf-8')

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, response_headers)

    return [response]
