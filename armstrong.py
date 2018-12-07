def armstrong(s):
	m=s
	c=0
	while(s>0):
		r=s%10
		c=c+r**3
		s=s/10
	if(c==m):
		print c
n=input("enter the range: ")
print "The armstrong numbers in given range are -->\v"
for i in range(1,n+1):
	armstrong(i)
