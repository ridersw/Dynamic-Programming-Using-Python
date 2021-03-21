#Find the nth Fibonacci Number

#C:\Users\Shashiraj Walsetwar\Desktop>python dynamicProgramming.py
#102334155
#time required For Regular Method: 24.678236961364746
#102334155
#time required For DP Method: 0.0


import time

#regular Method
def fib(n):
	if n <= 2:
		return 1 
	
	return fib(n-1) + fib(n-2)
	
#DP Technique
def fibDP(n, memo = {}):
	if n in memo:
		return memo[n]
	if n <= 2:
		return 1 
	
	memo[n] = fibDP(n-1) + fibDP(n-2)
	return memo[n]
	
	
	
if __name__ == "__main__":
	n = 40
	t1 = time.time()
	print(fib(n))
	t2 = time.time()
	print(f"time required For Regular Method: {t2 - t1}")
	
	n = 40
	t1 = time.time()
	print(fibDP(n))
	t2 = time.time()
	print(f"time required For DP Method: {t2 - t1}")