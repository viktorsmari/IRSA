import sqlite3
con = sqlite3.connect('database.db') # Warning: This file is created in the current directory
print "Connection successful."

# con.execute(''' 
# 	CREATE TABLE vb_servicerequest (
		# id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		# serialno VARCHAR(100),
		# client INT NOT NULL REFERENCES vb_client(id),
		# status INT NOT NULL REFERENCES vb_status(id),
		# make INT NOT NULL REFERENCES vb_make(id),
		# color INT NOT NULL REFERENCES vb_color(id),
		# problemdesc TEXT,
		# solutiondesc TEXT,
		# shortdesc VARCHAR(255),
		# enteredby INT NOT NULL REFERENCES vb_users(id),
		# assignedto INT NOT NULL REFERENCES vb_users(id),
		# received DATE,
		# started DATE,
		# finished DATE	
# 	);
# ''')



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
