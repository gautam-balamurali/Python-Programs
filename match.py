#Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it.  Your function should ignore all other symbols that appear in s.  Your function should return True if s has matched brackets and False if it does not.

#Here are some examples to show how your function should work.

#>>> matched("zb%78")
#True
#>>> matched("(7)(a")
#False
#>>> matched("a)*(?")
#False
#>>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
#True

def matched(s):
	l,o,c=len(s),0,0
	for i in range(0,l):
		ch=s[i]
		if(ord(ch)==40):
			m=i
			o+=1
		elif(ord(ch)==41):
			p=i
			c+=1
	if(m<p and o==c):
		return True
	else:
		return False
k=raw_input("enter the string ")
print matched(k)
