def canSum(target, numbers, memo = {}):

	if target in memo:
		return memo[target]
	
	if target == 0:
		return True
	
	if target < 0:
		return None
	
	
	for num in numbers:
		remainder = target - num
		remain = canSum(remainder, numbers, memo)
		
		if remain == True:
			memo[target] = True
			return memo[target]
	
	memo[target] = False
	return False
	
if __name__ == "__main__":
	print(canSum(200, [2, 3]))