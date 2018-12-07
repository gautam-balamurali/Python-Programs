






"""def perfect(n):
    A positive integer n is said to be perfect if the sum of the factors of n, other than n itself, add up to n. For instance 6 is perfect since the factors of 6 are {1,2,3,6} and 1+2+3=6. Likewise, 28 is perfect because the factors of 28 are {1,2,4,7,14,28} and 1+2+4+7+14=28.

    Write a Python function perfect(n) that takes a positive integer argument and returns True if the integer is perfect, and False otherwise.

    Here are some examples to show how your function should work.

    >>> perfect(6)
    True
    >>> perfect(12)
    False
    >>> perfect(28)
    True

    For an expression with parentheses, we can define the nesting depth as the maximum number of parentheses that are open when reading the expression from left to right. For instance, the nesting depth of "(33+77)(44-12)" is 1, while the nesting depth of "(a(b+c)-d)(e+f)" is 2.

    Write a Python function depth(s) that takes a string containing an expression with parentheses and returns an integer, the nesting depth of s. You can assume that s is well-parenthesized: that is, that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it.

    Here are some examples to show how your function should work.

    >>> depth("22")
    0
    >>> depth("(a+b)(a-b)")
    1
    >>> depth("(a(b+c)-d)(e+f)")
    2

    Write a function sumsquares(l) that takes as input a list of integers and retuns the sum of all the perfect squares in l.

    Here are some examples to show how your function should work.

    >>> sumsquares([1,4,9])
    14
    >>> sumsquares([10,11,12,15])
    0
    >>> sumsquares([16,20,25,30,625])
    666"""


  sum=0
  for i in range(1,n):
    if(n%i==0):
      sum=sum+i
  if(sum==n):
    return True
  else:
    return False

  
def depth(s):
    count = 0
    max = 0
    for character in s:
        if character == "(":
            count += 1
            if count > max:
                max = count
        elif character == ")":
            count -= 1
    return max    
  
def sumsquares(l):
  import math
  sum=0
  for num in l:
    if num == int(math.sqrt(num)) ** 2:
      sum+=num
  return sum
