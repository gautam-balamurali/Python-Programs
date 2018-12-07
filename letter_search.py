w=raw_input("enter the word ")
s=raw_input("enter the letter ")
c=0
for i in w:
	if (i==s):
		c+=1
if (c>0):
	print "found"
else:
	print "not found"
		
