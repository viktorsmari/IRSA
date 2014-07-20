import sqlite3
con = sqlite3.connect('database.db') # Warning: This file is created in the current directory
print "Connection successful."

con.execute(''' 
	CREATE TABLE vb_servicerequest (
		
	);
''')



con.execute('''
	CREATE TABLE vb_client (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name VARCHAR(50),
		kt VARCHAR(10),
		email VARCHAR(50),
		phone VARCHAR(10),
		address VARCHAR(100),
		postalcode VARCHAR(8)
	);
''')
print "Created table vb_client!"

#Create two test dummy
con.execute('''INSERT into vb_client VALUES(1, 'Viktor', '0903843259', 'viktor@rrr.rr', '8659309', 'Bolagata', '900');''')
con.execute('''INSERT into vb_client VALUES(2, 'Muggi', '654354489', 'mag@bleb.io', '8452652', 'Njoasdf', '255');''')


con.commit()
con.close()
