def canSumArray(target, numbers, memo = {}):
	if target in memo:
		return memo[target]
	
	if target == 0:
		return [] 
		
	if target < 0:
		return None
		
	for number in numbers:
		remainder = target - number
		remainderArray = canSumArray(remainder, numbers)
		#print(f"remainderArray: {remainderArray}")
		if remainderArray is not None:
			remainderArray.append(number)
			memo[target] = remainderArray
			return memo[target]
	
	memo[target] = None
	return memo[target]
	
	
if __name__ == "__main__":
	numbers = [21, 3]
	target = 700
	print(canSumArray(target, numbers))
	
#return an array that gives sum equal to target sum