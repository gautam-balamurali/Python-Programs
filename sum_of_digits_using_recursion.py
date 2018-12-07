def digits(n):
	if(n==0):
		return 0
	else:
		p=n
		n=n%10
		return(n+digits(p/10))
num=input("enter the no.: ")
m=num
sum=digits(num)
print "sum of the digits of %i= "%(m),sum