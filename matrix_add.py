m1,m2,m3,m4=[],[],[],[]
r=input("enter the no. of rows ")
c=input("enter the no. of columns ")
print "for first matrix "
for i in range(0,r):
	m1.append([])
	for j in range(0,c):
		m1[i].append(input("enter value "))
print "for second matrix "
for i in range(0,r):
	m2.append([])
	for j in range(0,c):
		m2[i].append(input("enter value "))

for i in range(0,r):
	m3.append([])
	for j in range(0,c):
		m3[i].append(m1[i][j]+m2[i][j])
for i in range(0,r):
	m4.append([])
	for j in range(0,c):
		m4[i].append(m1[i][j]-m2[i][j])
print "after addition"
for i in range(0,r):
	for j in range(0,c):
		print m3[i][j],
	print
print "after subtraction"
for i in range(0,r):
	for j in range(0,c):
		print m4[i][j],
	print
