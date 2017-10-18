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
names = c.fetchall()
#print names

#Get student's averages
def getAverage(studentid):
	avgsum = 0;
	count = 0;
	for each in gradeList:
		if studentid == each[1]:
			avgsum += each[0]
			count += 1
	return avgsum / count

#print getAverage(1)

#Create table
def createTable():
        c.execute("drop table peeps_avg")
        command = "CREATE TABLE peeps_avg (id INTEGER, avg INTEGER);"
        c.execute(command)
        for each in names:
                avg = getAverage(each[1])
                command = 'INSERT INTO peeps_avg VALUES(' + str(each[1]) + ',' + str(avg) + ');'
                #print(command)
                c.execute(command)
                
createTable()
        
