def gridTraverler(m, n, memo = {}):
	if m == 1 and n == 1:
		return 1
	
	if m == 0 or n == 0:
		return 0
		
	if (m , n) in memo:
		return memo[m, n]
	memo[m, n] = gridTraverler(m - 1, n) + gridTraverler(m, n - 1)
	return memo[m, n]
	
	
if __name__ == "__main__":
	print(gridTraverler(1,1))
	print(gridTraverler(2,3))
	print(gridTraverler(3,2))
	print(gridTraverler(3,3))
	print(gridTraverler(18,18))
	
#Grid Traveling Problem
#Number of Ways you can travel from Top left Corner to bottom right corner using only down and right direction while travelling