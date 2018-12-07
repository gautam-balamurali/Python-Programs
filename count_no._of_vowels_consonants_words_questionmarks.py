s=raw_input("enter the string ")
v=0
c=0
w=0
q=0
s=s+' '
s=s.lower()
n=len(s)
for i in range(0,n):
	ch=s[i]
	if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
		v=v+1
	if(ch!='a' and ch!='e' and ch!='i' and ch!='o' and ch!='u' and ch!=' ' and ch!='?'):
		c=c+1
	if(ch==' '):
		w=w+1
	if(ch=='?'):
		q=q+1
print "vowels= ",v
print "consonants= ",c
print "words= ",w
print "question marks= ",q
