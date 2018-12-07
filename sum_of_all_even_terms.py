#to find sum of all even terms in a group of n numbers

s=0
a=[]
n=input("enter the limit ")
for i in range(0,n):
	b=input("enter the no. ")
	a.insert(i,b)


for i in range(0,n):
	if(i%2==0):
		s=s+a[i]
print "sum is= ",s
