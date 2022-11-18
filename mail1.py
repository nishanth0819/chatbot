import smtplib
OWN_EMAIL="mn9654@srmist.edu.in"
OWN_PASSWORD="@Nani0819"
'''def sendmail(empid,assempid,typeofwork,noofdays,recvmail,assigner,assignedto):
    email_message="\nWork assigned empid :"+assempid+"\nWork assigned empname :"+assigner
    email_message=email_message+"\nType of Work :"+typeofwork+"\nDeadline :"+noofdays+" days"
    print(email_message)
    print(type(email_message))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL,OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL,to_addrs=recvmail,msg=email_message)'''
def sendmail(empid,assempid,typeofwork,noofdays,recvmail,assigner,assignedto,g):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('mn9654@srmist.edu.in','@Nani0819')
    email_message="\nWork assigned empid :"+empid+"\nWork assigned empname :"+assigner
    email_message=email_message+"\nType of Work :"+typeofwork+"\nDeadline :"+noofdays+" days"
    email_message=email_message+"\nDeadline Date : "+g
    server.sendmail('mn9654@srmist.edu.in',recvmail,email_message)
    
    
