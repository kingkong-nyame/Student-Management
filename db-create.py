import sqlite3

db_locale = 'student.db'
con = sqlite3.connect(db_locale)
c = con.cursor()

c.execute("""
SELECT * FROM contact_details
cd 
""")
student_info = c.fetchall()

for student in student_info:
    print(student)


con.commit()
con.close()