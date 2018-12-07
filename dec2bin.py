a=[]
n=input("Enter the no.--> ")
while(n>0):
	r=n%2
	a.append(r)
	n=n/2
a.reverse()
for i in a:
	print i,
