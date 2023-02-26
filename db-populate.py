import sqlite3

db_locale = 'student.db'
con = sqlite3.connect(db_locale)
c = con.cursor()

c.execute("""
INSERT INTO contact_details (firstname, surname, class, street_address)VALUES
('Emmanuel', 'Gyimah', 'Information Technology level 300', 'Fiapre-Sunyani' ),
('Stefan', 'Asante', 'Information Technology level 300', 'Fiapre-Sunyani' ),
('Samuel', 'Agyei', 'Information Technology level 300', 'Fiapre-Sunyani' )
""")

con.commit()
con.close()