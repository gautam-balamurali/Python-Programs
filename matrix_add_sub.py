m1,m2,m3,m4=[],[],[],[]
r=input("Enter the no. of rows ")
c=input("Enter the no. of columns ")
print "Enter the values in 1st matrix-->"
for i in range(r):
	m1.append([])
	for j in range(c):
		m1[i].append(input("enter value: "))
print "Enter the values in 2nd matrix-->"
for i in range(r):
	m2.append([])
	for j in range(c):
		m2[i].append(input("enter value: "))
for i in range(r):
	m3.append([])
	for j in range(c):
		m3[i].append(m1[i][j]+m2[i][j])
for i in range(r):
	m4.append([])
	for j in range(c):
		m4[i].append(m1[i][j]-m2[i][j])
print "1st matrix-->"
for i in range(r):
	for j in range(c):
		print m1[i][j],
	print
print "2nd matrix-->"
for i in range(r):
	for j in range(c):
		print m2[i][j],
	print
print "After addition-->"
for i in range(r):
	for j in range(c):
		print m3[i][j],
	print
print "After Subtraction-->"
for i in range(r):
	for j in range(c):
		print m4[i][j],
	print

