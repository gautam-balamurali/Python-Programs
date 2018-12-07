a=[]
def inp():
	c=input("Enter the number of books-> ")
	l=len(a)
	for i in range(l,c):
		a.append([])
		idb=raw_input("Enter the id-> ")
		name=raw_input("Enter the title-> ")
		auth=raw_input("Enter the author-> ")
		a[i]=[idb,name,auth]
	print a
	mains()
def disp():
	l=len(a)
	for i in range(l):
		print a[i]
	mains()
def auth():
	l=len(a)
	k=raw_input("Enter the author-> ")
	for i in range(l):
		if a[i][2]==k:
			print a[i]
	mains()
def spb():
	l=len(a)
	k=raw_input("Enter the id-> ")
	for i in range(l):
		if a[i][0]==k:
			print a[i]
	mains()
def exit():
	print "Your program exited"
def mains():
	print("input your choice \n To enter book details:a  \n To display book details:b  \n To search by author:c  \n to search by id:d  \n to exit:e  ")
	r=raw_input("Enter-> ")
	if r=="a":
		inp()
	elif r=="b":
		disp()
	elif r=="c":
		auth()
	elif r=="d":
		spb()
	elif r=="e":
		exit()
	else:
		print "Bad Choice"
mains()
 

