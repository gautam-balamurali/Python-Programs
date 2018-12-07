n=input("Enter the range--> ")
a,b=-1,1
for i in range(0,n):
	c=a+b
	a=b
	b=c
	if(i!=n-1):
		print c,',',
	else:
		print c,'.',
	
