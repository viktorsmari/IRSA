from bottle import route, run, template, get, post, request, static_file, redirect
import sqlite3

#### Basic routes ####

@route('/')
def index():
	# This page really does nothing..
	return template('index.tpl')

@route('/new', method='GET')
def create_new():
	if request.GET.get('save','').strip():
		conn = sqlite3.connect('database.db')
		c = conn.cursor()

		# This needs refactoring, SQL inject safe?

		ssn = request.GET.get('ssn','').strip()
		name = request.GET.get('name','').strip()
		email = request.GET.get('email','').strip()
		phone = request.GET.get('phone','').strip()
		address = request.GET.get('address','').strip()
		pobox = request.GET.get('pobox','').strip()
		c.execute("INSERT INTO vb_client (name,kt,email,phone,address,postalcode) VALUES (?,?,?,?,?,?)",(ssn,name,email,phone,address,pobox) )

		# Service RQ table
		readydate = request.GET.get('readydate','').strip()
		serialnumber = request.GET.get('serialnumber','').strip()
		make = request.GET.get('make','').strip()
		shortdesc = request.GET.get('shortdesc','').strip()
		color = request.GET.get('color','').strip()		
		problemdesc = request.GET.get('problemdesc','').strip()		
		c.execute("INSERT INTO vb_servicerequest (finished,serialno,make,shortdesc,color,problemdesc) VALUES (?,?,?,?,?,?)", (readydate,serialnumber,make,shortdesc,color,problemdesc) )

		conn.commit()
		conn.close()
		print ("Inserted into vb_client...")

	redirect("/clients")
	# return template('create.tpl')

@route('/create', method='GET')
def createpage():

	return template('create.tpl')

@route('/overview')	
def overviewpage():

	# Get top page statistics
	conn = sqlite3.connect('database.db')
	c = conn.cursor()

	# Why do I need to assign values to this list beforehand ?!
	stats = [9,8,7,6]
	stats[0] = c.execute("select count(*) from vb_servicerequest where status Like 0;").fetchone()[0]
	stats[1] = c.execute("select count(*) from vb_servicerequest where status Like 1;").fetchone()[0]
	stats[2] = c.execute("select count(*) from vb_servicerequest where status Like 2;").fetchone()[0]
	stats[3] = c.execute("select count(*) from vb_servicerequest where status Like 3;").fetchone()[0]


	c.execute("SELECT * FROM vb_servicerequest")
	result = c.fetchall()
	c.close()

	return template('overview.tpl', rows=result,statusrows=stats)

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
