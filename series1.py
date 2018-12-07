#1-x^2/2!+x^4/4!-x^6/6!+....n terms

s1=1
s2=0
n=input("enter the range ")
x=input("enter the value of x ")
for i in range(4,n+1,4):
	f=1
	for j in range(1,i+1):
		f=f*j
	s1=s1+((x**i)/f)
for i in range(2,n+1,4):
	f=1
	for j in range(1,i+1):
		f=f*j
	s2=s2+((x**i)/f)
s=s1-s2
print "sum of series= ",s
