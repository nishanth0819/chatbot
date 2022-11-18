import sqlite3
def connect(empid,assempid,typeofwork,noofdays):
    conn=sqlite3.connect('test1.db')
    """conn.execute(''' CREATE TABLE WORK1
                     ( ASSID VARCHAR(19),
                       WID VARCHAR(19),
                       TYPEWORK VARCHAR(19),
                       NOOFDAYS INT
                       )''')"""
    
    sql='INSERT INTO WORK1 (ASSID,WID,TYPEWORK,NOOFDAYS) VALUES ("{0}","{1}","{2}","{3}")'.format(empid,assempid,typeofwork,noofdays)
    conn.execute(sql)
    cursor=conn.execute("SELECT ASSID,WID,TYPEWORK,NOOFDAYS fROM WORK1")
    conn.commit()