#!/usr/bin/python

import smtplib


sender = ''
receivers = ['']
var=(1,2,3,4,5,6)
message = """From: From Person <>
To: To Person <>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('imap.gmail.com', 587)
   smtpObj.starttls()
   smtpObj.login("","")
   smtpObj.sendmail(sender, receivers, message) 
   smtpObj.quit()        
   print "Successfully sent email"
except Exception as ex:
   print "Error: unable to send email",ex
