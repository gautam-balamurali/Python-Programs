#program to create student record using dictionary
s={}
n=input("enter the no. of students ")
for i in range(0,n):
	rolnm=raw_input("enter the roll number-%d"%(i))
	name=raw_input("name of student-%d"%(i))
	mark=raw_input("mark of student-%d"%(i))
	branch=raw_input("branch of student-%d"%(i))
	s[name]=[rolnm, mark, branch]
print "RollNo.\tName\tMark\tBranch"
lst=[]
lst=s.keys()
lst.sort()
for i in s:
	lst=s[i]
	print str(i)+"\t"+str(lst[0])+"\t"+str(lst[1])+"\t"+str(lst[2])

