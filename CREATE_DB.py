import sqlite3
con = sqlite3.connect('database.db') # Warning: This file is created in the current directory
print "Connection successful."

## Table is missing all foreign keys
## just a test table
con.execute(''' 
	CREATE TABLE vb_servicerequest (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		serialno VARCHAR(100),
		client INT ,
		status INT ,
		make INT ,
		color INT,
		problemdesc TEXT,
		solutiondesc TEXT,
		shortdesc VARCHAR(255),
		enteredby INT ,
		assignedto INT,
		received DATE,
		started DATE,
		finished DATE	
	);
''')
print "Created vb_servicerequest!"
con.execute(''' INSERT into vb_servicerequest VALUES 
		(1,'S1231', 1,2,3,4,'Broken dong','replaced it', 'short desc',1,1,'2012-11-11','2011-10-10','2010-08-07')
	''')

con.execute('''
	CREATE TABLE vb_client (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(50),
		kt VARCHAR(10),
		email VARCHAR(100),
		phone VARCHAR(10),
		address VARCHAR(100),
		postalcode VARCHAR(8)
	);
''')
print "Created table vb_client!"

#Create two test dummy
con.execute('''INSERT into vb_client VALUES(1, 'Viktor', '0903843259', 'viktor@rrr.rr', '5659009', 'Bolagata', '900');''')
con.execute('''INSERT into vb_client VALUES(2, 'Muggi', '654354489', 'mag@blreeb.io', '5452652', 'Njoasdf', '255');''')

con.commit()
con.close()
