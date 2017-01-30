from urlparse import parse_qs, urlparse

def app(environ, start_response):
	o = parse_qs(urlparse("?" + str(environ.get('QUERY_STRING', ''))).query, keep_blank_values=True)
	response = ''    
	for key in list(sorted(o.keys())):
		for val in list(o[key]): 
			response += str(key) + "=" + str(val) + "\n"
	status = '200 OK'
	response_headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, response_headers)
	return [response]
