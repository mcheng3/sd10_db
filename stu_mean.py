import sqlite3

db = sqlite3.connect("students.db")
c = db.cursor()

#Look up students' grades
command = "SELECT mark, id FROM courses"
c.execute(command)
gradeList =  c.fetchall()
print(gradeList)
def getAverage(studentid):
	avgsum = 0;
	count = 0;
	for each in gradeList:
		if studentid == each[1]:
			avgsum += each[0]
			count += 1
	return avgsum / count

print getAverage(1)
		 
