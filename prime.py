def prime(n):
	for i in range(2,n/2):
		k=n%i
		if(k==0):
			print "not prime"
			return
	print "prime"
	return
		
	
s=input("Enter the no. ")
if(s==2):
	print "prime"
else:
	prime(s)

