def perfect(n):
	s=0
	m=n
	for i in range(1,n):
		if(n%i==0):
			s=s+i
	if(s==m):
		print "perfect no."
	else:
		print "not perfect no."
k=input("enter the no. ")
perfect(k)
