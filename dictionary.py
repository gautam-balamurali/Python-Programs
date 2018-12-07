#to create a name list of students in alphabetical order
stud={} #to initialise dictionary
n=input("enter the number of students ")
for i in range(0,n):
	a=raw_input("enter the name of students ")
	stud[a]=input("enter the mark ")
print stud
b=[]
b=stud.keys() #append each key value pair to a list named b
print b
b.sort()
for i in range(n):
	print("%s \t %d"%(b[i],stud[b[i]]))
