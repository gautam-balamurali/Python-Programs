n=input("Enter the no of students : ")

stud={}

for i in range(n):
	roll=input("Enter the roll no : ")
	name=raw_input("Enter the name : ")
	mark1=input("Enter the mark in subject 1 : ")
	mark2=input("Enter the mark in subject 2 : ")
	mark3=input("Enter the mark in subject 3 : ")
			
	stud[roll]=[name,mark1,mark2,mark3]



search=input("Enter the roll no whose record is to be searched : ")

#print stud[search]
arr=[]
arr=stud[search]
per=(arr[1]+arr[2]+arr[3])/3.0
print "Name Roll mark1 Mark2 Mark3 Avg"
print str(arr[0])+"     "+str(search)+"    "+str(arr[1])+"    "+str(arr[2])+"    "+str(arr[3])+"    "+str(per)

