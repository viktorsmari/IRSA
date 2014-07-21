IRSA
=====

Repair Shop Assistant running on Python / Bottle


Ubuntu install:

Clone git repo:

    git clone https://github.com/viktorsmari/IRSA
 
You need sqlite3 for the database and python-pip to install bottle

    sudo apt-get install sqlite3 python-pip
    sudo pip install bottle
 
To create a database with some dummy records, run first:
	
	python CREATE_DB.py


Run it from the directory:

    python irsa.py

and visit localhost:8080 from browser
   