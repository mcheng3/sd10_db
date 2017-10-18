import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

courses = csv.DictReader(open("data/courses.csv"))
people = csv.DictReader(open("data/peeps.csv"))

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);" #put SQL statement in this string
c.execute(command)    #run SQL statement
command = "CREATE TABLE people (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);"
c.execute(command)

for row in courses:
	cmd = "INSERT INTO courses VALUES ('" + row['code'] + "', '" + row['mark'] +  "', '" + row['id'] + "');"
	#print cmd
	c.execute(cmd)

for row in people:
	cmd = "INSERT INTO people VALUES ('" + row['name'] + "', '" + row['age'] +  "', '" + row['id'] + "');"
	#print cmd
	c.execute(cmd)

#==========================================================
db.commit() #save changes
db.close()  #close database


