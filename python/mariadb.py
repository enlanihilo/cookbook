from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

today = datetime.now()

"""
	Docs:
		dev.mysql.com/doc/connector-python/en/
		mariadb.com/kb/en/library/a-mariadb-primer/
		wiki.archlinux.org/index.php/MariaDB
"""

#1. login with db user
#2. select database (e.g: use test;)

#mariadb default port # = 3306
config = {
	"user" : "tester",
	"password" : "",
	"host" : "localhost",
	"database" : "test"
}
	

try:
	cnx =mysql.connector.connect(**config)
	cursor = cnx.cursor()
except:
	raise errorcode

#3. manipulate tables



mariadb_cmd = "SELECT * FROM employees;"

#executing commands


TABLES = {}
TABLES["employees"] = ("""
	CREATE TABLE IF NOT EXISTS employees (
	 `emp_no` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
	 `birth_date` date NOT NULL,
	 `first_name` varchar(15) NOT NULL,
	 `last_name` varchar(15) NOT NULL,
	 `gender` enum('M', 'F') NOT NULL,
	 `hire_date` date NOT NULL
	 );
""")

#create table
cursor.execute(TABLES["employees"])

#populate table
emp1 = {
	"first_name" : "Geert",
	"last_name" : "Vanderkelen",
	"hire_date" : "2019-08-03",
	"gender" : "M",
	"birth_date" : "1994-07-06"
}

emp2 = {
	"first_name" : "Simona",
	"last_name" : "Venture",
	"hire_date" : "2012-10-25",
	"gender" : "F",
	"birth_date" : "1977-11-01"
}

emp3 = {
	"first_name" : "Leone",
	"last_name" : "Brizzo",
	"hire_date" : "2009-06-10",
	"gender" : "M",
	"birth_date" : "1982-10-08"
}

add_employee = (f"""
		INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) 
		VALUES (
			'{emp1["first_name"]}', '{emp1["last_name"]}', '{emp1["hire_date"]}', '{emp1["gender"]}', '{emp1["birth_date"]}'
		);
""")

cursor.execute(add_employee)

add_employee = (f"""
		INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) 
		VALUES (
			'{emp2["first_name"]}', '{emp2["last_name"]}', '{emp2["hire_date"]}', '{emp2["gender"]}', '{emp2["birth_date"]}'
		);
""")

cursor.execute(add_employee)

add_employee = (f"""
		INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) 
		VALUES (
			'{emp3["first_name"]}', '{emp3["last_name"]}', '{emp3["hire_date"]}', '{emp3["gender"]}', '{emp3["birth_date"]}'
		);
""")

cursor.execute(add_employee)
#for result in cursor.execute(mariadb_cmd, multi=True):
#	print(result.fetchall())

emp_no = cursor.lastrowid

cnx.commit()
cursor.close()
cnx.close()


