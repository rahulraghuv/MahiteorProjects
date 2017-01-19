import csv
filename="Rahul_raghuvanshi_test_file.txt"
csvFile=open(filename)
csvReader=csv.reader(csvFile)
print csvReader
csvList=list(csvReader)
print csvList
listData=[]
var=i=0
for data in csvList:
    for j in data:
	var=var+int(j)
    listData.append(var)
    i+=1
print listData
