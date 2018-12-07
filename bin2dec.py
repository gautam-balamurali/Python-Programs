def bindec(s1):
	dec=0
	t=0
	s=int(s1)
	while(s>0):
		p=s%10
		dec=dec+p*(2**t)
		#p=p*(2**t)
		t+=1		
		s=s/10
		#dec=dec+p
	print "decimal number is",dec
b=raw_input("enter the binary nmbr")
bindec(b)
		
