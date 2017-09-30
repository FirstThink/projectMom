from bottle import run, get, post, request

@get('/')
@get('/home')
def default_page():
	return '''
		<form action="/home" method="POST">
			Search: <input name="query" type="text fields">

			<input value="Submit" type="submit">
		</form>
		'''
@post('/home')							# submit button induces the call of search_query()
def search_query():
	query = request.forms.get('query')	# input string stored in the variable QUERY
	if query == '':						# if there is no input
		return "<p>Please enter something.</p>"
	else:
		# where all the results go (tables, top 20 history, URLs, etc)
		return query
		
run(host='localhost', port=8080, debug=True)	# runs the server
