s=raw_input("enter the string ")
s=s.lower()
s1=""
v=0
n=len(s)
for i in range(0,n):
	ch=s[i]
	if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
		v=v+1
	else:
		s1=s1+ch
print "vowels= ",v
print "new string= ",s1


		
		

