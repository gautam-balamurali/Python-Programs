def sum(n):
	if(n<=0):
		return 0
	elif(n%2!=0):
		return(n+sum(n-2))
	elif(n%2==0):
		p=n-1
		return(p+sum(p-2))
num=input("enter last limit")
s=sum(num)
print "sum of odd numbers is ",s