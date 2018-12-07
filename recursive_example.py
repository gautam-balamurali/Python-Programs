def fact_rec(x):
	if x==1 :
		return 1
	else:
		return(x*fact_rec(x-1))
a=input("enter the nmbr ")
print "factorial is ",fact_rec(a)


