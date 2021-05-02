def howSum(targetSum, numbers, memo = {}):
	if targetSum in memo:
		return memo[targetSum]

	if targetSum == 0:
		return []
		
	if targetSum < 0:
		return None
		
	for number in numbers:
		#print(f"checking for {number}")
		remainder = targetSum - number
		remainderResult = howSum(remainder, numbers, memo)
		if remainderResult != None:
			remainderResult.append(number)
			memo[targetSum] = remainderResult
			return memo[targetSum]
	
	memo[targetSum] = None
	return None
	
	
if __name__ == "__main__":
	targetSum = 7
	numbers = [2, 3]
	
	#targetSum = 1000
	#numbers = [7, 14]
	
	print(howSum(targetSum, numbers))
	