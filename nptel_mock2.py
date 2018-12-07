 """Write three Python functions as specified below. Paste the text for all three functions together into the submission window.

    You may define additional auxiliary functions as needed.
    In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
    For each function, there are some public test cases and some (hidden) private test cases.
    "Compile and run" will evaluate your submission against the public test cases.
    "Submit" will evaluate your submission against the hidden private test cases and report a score on 100. There are 9 private testcases in all, 3 per function, each with equal weightage.
    Ignore warnings about "Presentation errors". 

    Define a Python function ascending(l) that returns True if each element in its input list is at least as big as the one before it.

    Here are some examples to show how your function should work.

    >>> ascending([])
    True
    >>> ascending([3,3,4])
    True
    >>> ascending([7,18,17,19])
    False

    A list of integers is said to be a valley if it consists of a sequence of strictly decreasing values followed by a sequence of strictly increasing values. The decreasing and increasing sequences must be of length at least 2. The last value of the decreasing sequence is the first value of the increasing sequence.

    Write a Python function valley(l) that takes a list of integers and returns True if l is a valley and False otherwise.

    Here are some examples to show how your function should work.

    >>> valley([3,2,1,2,3])
    True
    >>> valley([3,2,1])
    False
    >>> valley([3,3,2,1,2])
    False

    A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix

    1  2  3
    4  5  6 

    would be represented as [[1,2,3],[4,5,6]].

    The transpose of a matrix makes each row into a column. For instance, the transpose of the matrix above is

    1  4  
    2  5
    3  6

    Write a Python function transpose(m) that takes as input a two dimensional matrix using this row-wise representation and returns the transpose of the matrix using the same representation.

    Here are some examples to show how your function should work. You may assume that the input to the function is always a non-empty matrix.

    >>> transpose([[1,4,9]])
    [[1], [4], [9]]

    >>> transpose([[1,3,5],[2,4,6]])
    [[1,2], [3,4], [5,6]]
    0 
    >>> transpose([[1,1,1],[2,2,2],[3,3,3]])
    [[1,2,3], [1,2,3], [1,2,3]]

Select the Language for this assignment.
"""

def ascending(l):
  n=len(l)
  for i in range(0,n-1):
    if(l[i+1]<l[i]):
      return False
	
  return True



def valley(l):
  if(len(l)==0):
    return(True)
  if(len(l)==1):
    return(False)
  if(l[0]<l[1]):
    return(False)
  for i in range(0,len(l)-1):
    if(l[i]<l[i+1]):
      pos=i
      break
    if(l[i]==l[i+1]):
      return(False) 
  else:
    return(False)
  for i in range(pos,len(l)-1):
    if(l[i]>=l[i+1]):
      return(False)
  return(True)

def transpose(m):
  if not m:
    return []
  return [ [ row[ i ] for row in m ] for i in range( len( m[ 0 ] ) ) ]

