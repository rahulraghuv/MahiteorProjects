# -*- coding: utf-8 -*-
from django.db import models
import csv


class Document(models.Model):
    docfile = models.FileField()

class FileData():
    def __init__(self,inputData,output1,output2):
	self.input=inputData
        self.output1=output1
	self.output2=output2
    def processData(self,algo):
        if algo == 1:
	    self.algo1(self.inputData,self.output1,self.output2)
	else:
            self.algo2(self.inputData,self.output1,self.output2)
    def algo1(self,inputData,output1,output2):
             pass
    def algo1(self,inputData,output1,output2): 
             pass
    
