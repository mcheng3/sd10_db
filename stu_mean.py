import sqlite3

db = sqlite3.connect("students.db")
c = db.cursor()

#Create list with (mark, id) of each mark from courses

command = "SELECT mark, id FROM courses"
c.execute(command)
gradeList =  c.fetchall()
#print(gradeList)

#Create list with (name, id) from people
command = "SELECT name, id FROM people"
c.execute(command)
name = c.fetchall()
#print names

#Get student's averages
def getAverage(studentid):
	avgsum = 0.0;
	count = 0;
	for each in gradeList:
		if studentid == each[1]:
			avgsum += each[0]
			count += 1
	return avgsum / count

#print getAverage(1)

for each in name:
	print 'Student: ' + each[0] + ' ID: ' + str(each[1]) + ' Average: ' + "%5.2f"%getAverage(each[1])


#Create table
def createTable():
		#c.execute("DROP TABLE peeps_avg")
		command = "CREATE TABLE peeps_avg ( avg INTEGER, id INTEGER);"
		c.execute(command)
		for each in name:
			with db:
				avg = getAverage(each[1])
				command = 'INSERT INTO peeps_avg VALUES("%5.2f", "%d");'%(avg, each[1])
				c.execute(command)
		db.commit()

def updateAverage(studentid):
	command = "UPDATE peeps_avg SET avg = %5.2f WHERE id = %d"%(getAverage(studentid), studentid)
	c.execute(command)
	db.commit()

createTable()
updateAverage(5)

def updateGrades():
        command = "SELECT mark, id FROM courses"
        c.execute(command)
        gradeList =  c.fetchall()

def updateNames():
        command = "SELECT name, id FROM people"
        c.execute(command)
        name = c.fetchall()
        
def addRows(code, mark, studentid):
        command = "INSERT INTO courses VALUES('%s', %d, %d);"%(code, mark, studentid)
        c.execute(command)
        updateGrades()
        updateNames()
        updateAverage(studentid)
        db.commit()
addRows("softdev", 100, 10)
addRows("ceramics", 95, 10)


def printFetch():
	command = "SELECT * FROM peeps_avg;"
	c.execute(command)
	output = c.fetchall()
	print output
printFetch()



db.close()
