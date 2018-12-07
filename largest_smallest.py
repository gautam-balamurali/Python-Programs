#to find largest n smallest nmbrs in a list

a=input("enter the numbers in the list: ")
n=len(a)
l=a[0]
for i in range(0,n):
	if(l<a[i]):
		l=a[i]
s=a[0]
for i in range(0,n):
	if(s>a[i]):
		s=a[i]
print "largest is ",l
print "smallest is ",s