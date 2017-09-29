# Bottle tutorial at: (https://bottlepy.org/docs/dev/tutorial.html#request-routing)
# Access server by http://localhost:8080/

from bottle import run, route, get, post, request # or route

@get('/login') # or @route('/login'); default method of route() is GET
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    
@route('/static/<filename>')    # Sending a static file (such as an image or CSS file)
def server_static(filename):
    return static_file(filename, root='/path/to/your/static/files')     # cannot use relative path "./" 

run(host='localhost', port=8080, debug=True)	# runs the server
