from bottle import route, run, template, get, post, request, static_file
import sqlite3


#### Basic routes ####

@route('/')
def index():
	return template('index.tpl')

@route('/create')
def createpage():
	return template('create.tpl')

@route('/overview')	
def overviewpage():

	## Database example ##
	'''
	conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1';")
    result = c.fetchall()
    c.close()
  	'''

  	result='Lalala'
	
	return template('overview.tpl', rows=result)

@route('/clients')
def clientspage():
	conn = sqlite3.connect('database.db');
	c = conn.cursor()
	c.execute("SELECT * from vb_client")
	result = c.fetchall()
	c.close()

	return template('clients.tpl', rows=result)

@route('/users')
def userspage():
	return template('users.tpl')

@route('/settings')
def settingspage():
	return template('settings.tpl')





#### test ####

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






#### Serving CSS and JS files #####
@route('/static/<filename>')
def server_staticf(filename):
	return static_file(filename, root='static')

#### Errors ####
from bottle import error 
@error(404)
def error404(error):
	return '<p>You gotz 404 error</p> <a href="/">Go Back</a>'


# Reloader only in developer mode !
run(host='localhost', port=8080, debug=True, reloader=True)