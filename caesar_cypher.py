s=raw_input("enter the caesar cypher text to be decoded: ")
k=''
s=s.upper()
n=len(s)
for i in range(0,n):
	if(ord(s[i])>67 & ord(s[i])<91):
		ch=chr(ord(s[i])-3)
	elif(ord(s[i])>=65 & ord(s[i])<=67):
		ch=chr(ord(s[i])+23)
	elif(ord(s[i])==32):
		ch="_"
	k=k+ch
print "Decoded text is :",k.capitalize()
