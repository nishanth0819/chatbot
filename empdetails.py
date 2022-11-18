import sqlite3
def create():
    conn=sqlite3.connect('empdetails.db')
    conn.execute(''' CREATE TABLE WORK1
                     ( 
                        EID VARCHAR(19),
                        ENAME VARCHAR(19),
                        EMPEMAIL VARCHAR(19)
                       )''')

    sql='INSERT INTO WORK1 (EID,ENAME,EMPEMAIL) VALUES ("STS001","Nishanth","nishanthsai19@gmail.com")'
    conn.execute(sql)
    sql='INSERT INTO WORK1 (EID,ENAME,EMPEMAIL) VALUES ("STS002","Govardhan","nishanthsai19@outlook.com")'
    conn.execute(sql)
    sql='INSERT INTO WORK1 (EID,ENAME,EMPEMAIL) VALUES ("STS003","Sai","nishanthsai19@gmail.com")'
    conn.execute(sql)
    cursor=conn.execute("SELECT EID,ENAME,EMPEMAIL FROM WORK1")
    for row in cursor:
        print(row[0],end="")
        print(row[1],end="")
        print(row[2],end="")         
    conn.commit()
def findname(empid):
    conn=sqlite3.connect('empdetails.db')
    cursor=conn.execute("SELECT ENAME FROM WORK1 WHERE EID=?",(empid,))
    for row in cursor:
        return row[0]
def findemail(empid):
    conn=sqlite3.connect('empdetails.db')
    cursor=conn.execute("SELECT EMPEMAIL FROM WORK1 WHERE EID=?",(empid,))
    for row in cursor:
        return row[0]
    