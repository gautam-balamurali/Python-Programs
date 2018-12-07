def prime(k):
	f=1
	for i in range(2,k):
		if(k%i==0):
			f=0
	return f
n=input("enter last limit ")
print "Twin primes upto ",n,"are: "
for i in range(2,n-2):
	j=i+2
	a1=prime(i)
	a2=prime(j)
	if(a1==1 & a2==1):
		print i,"\t",j