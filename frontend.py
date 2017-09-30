from bottle import run, get, post, request

@get('/')
@get('/home')
def default_page():
	return '''
		<html>
		<head> <title> Athena </title> </head>
		<body>
			<h1> ATHENA </h1>
			<img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Athena_Giustiniani.jpg" width=374 height=649>	
			<form action="/home" method="POST">
				Search: <input name="query" type="text fields">
	
				<input value="Submit" type="submit">
			</form>
		</body>
		</html>
		'''
@post('/home')							# submit button induces the call of search_query()
def search_query():
	query = request.forms.get('query')	# input string stored in the variable QUERY
	if query == '':						# if there is no input
		return "<p>Please enter something.</p>"
	else:
		# where all the results go (tables, top 20 history, URLs, etc)
		return '''
			<table id="results">
				<tr>
					<td>the</td>
					<td>2</td>
				</tr>
				<tr>
					<td>lab</td>
					<td>3</td>
				</tr>
			</table>
			'''

run(host='localhost', port=8080, debug=True)	# runs the server
