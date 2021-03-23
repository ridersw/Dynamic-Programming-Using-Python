def bestSum(target, numbers):
	
	if target == 0:
		return []
		
	if target < 0:
		return None
		
	shortestArray = []
		
	for number in numbers:
		remainder = target - number
		remainderArray = bestSum(remainder, numbers)
		
		if remainderArray is not None:
			remainderArray.append(number)
			if len(remainderArray) < len(shortestArray) or shortestArray == []:
				shortestArray = remainderArray
			
	return shortestArray
	
	
if __name__ == "__main__":
	target = 8
	numbers = [1, 4, 5]
	print(bestSum(target, numbers))