#Define a Python function "alternating(l)" that returns True if the values in the input list alternately go up and down (in a strict manner).

#For instance:

#>>> alternating([])
#True

#>>> alternating([1,3,2,3,1,5])
#True

#>>> alternating([3,2,3,1,5])
#True

#>>> alternating([3,2,2,1,5])
#False

#>>> alternating([3,2,1,3,5])
#False

def alternating(l):
	if (len(l)==0 or len(l)==1):
		return True
	d=l[0]>l[1]
	for i in range(len(l)-1):
		if d:
			if not l[i]>l[i+1]:
				return False
		else:
			if not l[i]<l[i+1]:
				return False
		d=not d
	return True
k=input("enter list ")
print alternating(k)


