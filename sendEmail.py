#!/usr/bin/python

import smtplib


sender = 'rahulraghuv@gmail.com'
receivers = ['rahulraghuv@gmail.com']
var=(1,2,3,4,5,6)
message = """From: From Person <rahulraghuv@gmail.com>
To: To Person <yogendrakumarc@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
""",var

try:
   smtpObj = smtplib.SMTP('imap.gmail.com', 587)
   smtpObj.starttls()
   smtpObj.login("rahulraghuv@gmail.com","Synchronizedme3")
   smtpObj.sendmail(sender, receivers, message) 
   smtpObj.quit()        
   print "Successfully sent email"
except Exception as ex:
   print "Error: unable to send email",ex
