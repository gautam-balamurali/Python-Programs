'''A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix.  For instance, the matrix

1  2  3
4  5  6 

would be represented as [[1,2,3],[4,5,6]].

Write a Python function "matmult(m1,m2)" that takes as input two matrices using this row-wise representation and returns the matrix product m1*m2 using the same representation.

You may assume that the input matrices are well-formed and have compatible dimensions.

For instance:

>>> matmult([[1,2],[3,4]],[[1,0],[0,1]])
[[1,2],[3,4]]

>>> matmult([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]])
[[14, 32], [32, 77]]'''

def matmult(m1,m2):
	c=[[0 for row in range(len(m1))]for col in range(len(m2[0]))]
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			for k in range(len(m2)):
				c[i][j]+=m1[i][k]*m2[k][j]
	return c
s1=input("enter matrix ")
s2=input("enter 2nd matrix ")
print matmult(s1,s2)


