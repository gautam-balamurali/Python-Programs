a=[]
l=input("enter total no. of numbers ")
for i in range(0,l):
	b=input("enter the nmbr ")
	a.insert(i,b)
print a
n=len(a)
niv=0
z=0
for i in range(0,n):
	if(a[i]<0):
		niv=niv+1
	if(a[i]==0):
		z=z+1
print "total no. of negative terms= ",niv
print "total no. of zero terms= ",z
