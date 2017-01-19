# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from myproject.myapp.models import Document
from myproject.myapp.models import FileData
from myproject.myapp.forms import DocumentForm
import csv
import smtplib


def readCSV(name):
    filename=settings.MEDIA_ROOT+"/"+name
    print filename
    csvFile=open(filename)
    csvReader=csv.reader(csvFile,delimiter = ',')
    print csvReader
    csvList=tuple(csvReader)
    print csvList
    return csvList

def list(request):
    # Handle file upload
    name=""
    data=()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
#getting input/output parameters
	    input1=request.POST.get('input1')
	    output1=request.POST.get('input2')
    	    output2=request.POST.get('input3')
	    selectedAlgo=request.POST.get('algo')
    	    name = request.FILES['docfile'].name
	    email=tuple(request.POST.get('email'))
	    print name	    
            newdoc.save()
	    data=readCSV(name)
            print email
	    sendEmail(email,data)
	    print "data::",data
            # Redirect to the document list after POST
            return render(request,'phase2.html',{"data":data,"input1":input1,"input2":output1,"input3":output2,"algo":selectedAlgo})
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form,"data":data}
    )

def sendEmail(email,data):
	sender = 'rahulraghuv@gmail.com'
	message =data

	try:
   		smtpObj = smtplib.SMTP('imap.gmail.com', 587)
	        smtpObj.starttls()
	        smtpObj.login("rahulraghuv@gmail.com","Synchronizedme3")
                for receivers in email:
     		     smtpObj.sendmail(sender,['rahulraghuv@gmail.com'], message) 
   		smtpObj.quit()        
   		print "Successfully sent email"
	except Exception as err:
   		print "Error: unable to send email",err
