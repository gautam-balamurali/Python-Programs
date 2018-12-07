l=[]
n=input("enter the limit ")
for i in range(n):
	b=input("enter the element ")
	l.insert(i,b)
	tup1=tuple(l)
print"\n Unsorted List \n"
print tup1

for i in range(1,n):
	for j in range(0,n-1):
		if(l[j]>l[j+1]):
			l[j],l[j+1]=l[j+1],l[j]
tup2=tuple(l)
print"\n Sorted List \n"
print tup2
