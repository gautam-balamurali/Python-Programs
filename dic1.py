#students name in alphabetical
stud,b={},[]
n=input("enter d no. of stndts ")
for i in range(0,n):
	a=raw_input("enter the name of student ")
	stud[a]=input("entr the marks ")
print stud
b=stud.keys()
b.sort()
print "Name \t Mark "
for i in range(0,n):
	print "%s \t %d "%(b[i],stud[b[i]])

