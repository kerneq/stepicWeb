from urlparse import urlparse, parse_qs

def app(environ, start_response):
	urls = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
	body = []
  	for key, values in urls.items():
		for item in values:
			body.append(key + "=" + item + "\r\n")
	
	status = '200 OK'
	response_headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, response_headers)
	return body
