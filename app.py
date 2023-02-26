from flask import Flask, render_template
import sqlite3

app= Flask(__name__)
db_locale = 'student.db'

@app.route('/')
@app.route('/home')
def homepage():
    student_data = query_contact_details()
    return render_template('home.html', student_data=student_data)


def query_contact_details():
    con = sqlite3.connect(db_locale)
    c= con.cursor()
    c.execute("""
    SELECT * FROM contact_details
    
    """)
    student_data = c.fetchall()
    return(student_data)
@app.route('/add')
def add_student():
    return "<h1> Student added </h1>"

if __name__ == "__main__":
    app.run(debug=True)