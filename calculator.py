n=input("enter the no. of times you want to perform a particular task ")
print "                      1-Addition        "
print "                      2-Subtraction     "
print "                      3-Multiplication  "
print "                      4-Division        "
print "                      5-Exponentiation  "

ch=input("enter your choice-> ")
if(ch==1):
	for i in range(0,n):
		a=input("enter the number")
		b=input("enter the second number")
		s=a+b
		print a,"+",b,"=",s
	
if(ch==2):
	for i in range(0,n):
		a=input("enter the number")
		b=input("enter the second number")
		s=a-b
		print a,"-",b,"=",s
	
if(ch==3):
	for i in range(0,n):
		a=input("enter the number")
		b=input("enter the second number")
		s=a*b
		print a,"x",b,"=",s
	
if(ch==4):
	for i in range(0,n):
		a=input("enter the numerator")
		b=input("enter the denominator")
		s=a/b
		print a,"/",b,"=",s
	
if(ch==5):
	for i in range(0,n):
		a=input("enter the number")
		b=input("enter the power")
		s=a**b
		print a,"^",b,"=",s
	
else:
	print "Thank You. Try Again"