#student record
stud,lst={},[]
n=input("enter the no. of students ")
for i in range(1,n+1):
	r_no=raw_input("ENTER THE ROLL NO. OF STUDENT %d "%i)
	name=raw_input("enter the name of student %d "%i)
	mark=raw_input("enter the mark of student %d "%i)
	branch=raw_input("enter the branch of student %d "%i)
	stud[r_no]=[name,mark,branch]
print stud
print "Rollno\tName\tMark\tBranch"
for roll in stud:
	lst=stud[roll]
	print str(roll)+"\t"+str(lst[0])+"\t"+str(lst[1])+"\t"+str(lst[2])
