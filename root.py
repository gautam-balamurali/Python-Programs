def root(a1,b1,c1,d1):
	r1=(-b+d**0.5)/(2*a1)
	r2=(-b-d**0.5)/(2*a1)
	print "roots are"," ",r1,"&",r2
	return
a=input("enter coeff of x^2")
b=input("enter coeff of x")
c=input("enter constant")
d=b**2 - 4*a*c
if(d>0):
	print "real roots"
	root(a,b,c,d)
if(d==0):
	print "equal and real roots"
	root(a,b,c,d)
if(d<0):
	print "roots are complex"


