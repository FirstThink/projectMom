from bottle import run, route, get, post, request # or route

@get('/')
@get('/home')
def default_page():
	return '''
		<form action="/home" method="POST">
			Search: <input name="query" type="text fields">

			<input value="Submit" type="submit">
		</form>
		'''

run(host='localhost', port=8080, debug=True)	# runs the server

