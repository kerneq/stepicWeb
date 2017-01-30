from urlparse import urlparse, parse_qs

def app(environ, start_response):
	o = parse_qs("?" + urlparse(str(environ.get('QUERY_STRING', ''))).query, keep_blank_values=True)
	response = ''

	print(o)
	for key in list(sorted(o.keys())):
    		response += key + "=" + o[key][0] + "\n"
	status = '200 OK'
	response_headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, response_headers)
	return [response]
