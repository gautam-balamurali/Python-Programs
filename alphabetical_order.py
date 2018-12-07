def alpha(w):
	s=w
	w=w.lower()
	l=len(w)
	print "letters of word in alphabet %s are:"%(s)
	for i in range(65,91):
		for j in range(0,l):
			ch=w[j]
			if(ch==chr(i) or ch==chr(i+32)):
				print ch,
s=raw_input("Enter a word: ")
alpha(s)