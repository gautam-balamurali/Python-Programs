def vowels(w):
	w.lower()
	v=0
	l=len(w)
	for i in range(0,l):
		ch=w[i]
		if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
			v=v+1
	return v
w1=raw_input("enter a word: ")
s=w1
vowel=vowels(s)
print "total no. of vowels in %s are "%(w1),vowel
