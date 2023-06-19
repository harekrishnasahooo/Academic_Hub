import sqlite3
def create_db():
    con=sqlite3.connect(database="pqr.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text, description text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT , roll  text,name text,course text, marks_ob text, full_marks text, per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS attendance(aid INTEGER PRIMARY KEY AUTOINCREMENT , roll  text,name text,course text, class_done text, total_class text, per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT ,  f_name text, l_name text, contact text, Email text, question text, answer text, password text,email_id text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS trainee(tid INTEGER PRIMARY KEY AUTOINCREMENT ,  f_name text, l_name text, contact text, Email text, question text, answer text, password text, email_id text)")
    con.commit()


    con.close()


create_db()