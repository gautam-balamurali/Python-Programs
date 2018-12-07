b=1
while(b==1):
	print "1-Concat\n 2-UpperLOwer\n 3-DigitsChecker"
	ch=input("enter the choice ")
	if(ch==1):
		s=raw_input("enter the string ")
		s1=raw_input("enter the 2nd string ")
		print s,s1
	if(ch==2):
		s=raw_input("enter the string ")
		s2=""
		n=len(s)
		for i in range(0,n):
			ch=s[i]
			if(ch.isupper()):
				ch1=ch.lower()
				s2=s2+ch1
			if(ch.islower()):
				ch1=ch.upper()
				s2=s2+ch1
		print "new string is ",s2
	if(ch==3):
		s3=raw_input("enter the string ")
		n=len(s3)
		d=0
		for i in range(0,n):
			ch=s3[i]
			if(ch.isdigit()):
				d=d+1
		
		if(d>0):
			print "there are digits"
		else:
			print "there are no digits"
	b=input("if u want 2 continue press 1 ")
	if (b!=1):
		break

		
		

	
