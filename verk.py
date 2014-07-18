from bottle import route, run, template, get, post, request, static_file


# Index 
@route('/')
def index():
	return template('index.tpl')


@route('/hello/<name>')
def hello(name='Stranger'):
	return template('Hello {{name}}, sup?', name=name)


@route('/job/<jobnr:int>')	
def get_job_number(jobnr):
	assert isinstance(jobnr,int)
	return template("Getting job number {{jobnr}}", jobnr=jobnr)


@route('/object/<id:int>')	
def callback(id):
	assert isinstance(id,int)

@route('/show/<name:re:[a-z]+>')
def callback(name):
	assert name.isalpha()

@route('/static/<filename>')
def server_staticf(filename):
	return static_file(filename, root='static')


# Errors
from bottle import error 
@error(404)
def error404(error):
	return 'Some 404 error'


# Final line

run(host='localhost', port=8080, debug=True, reloader=True)