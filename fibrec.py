def fib(n):
	if (n<=1):
		return n
	else:
		return(fib(n-1)+fib(n-2))
nt=input("enter the nth fibonacci no. ")
for i in range(nt):
	print fib(i),
