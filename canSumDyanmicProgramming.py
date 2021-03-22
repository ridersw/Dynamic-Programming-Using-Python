import time

def canSum(target, numbers, memo = {}):
	#print(f"target: {target}")
	if target == 0:
		return True
		
	if target < 0:
		return False
		
	if target in memo:
		return True
		
	for number in numbers:
		remainder = target - number
		#print(f"Remainder: {remainder}")
		if(canSum(remainder, numbers)) == True:
			#memo[remainder, numbers] = True
			#print(f"memo: {memo}")
			memo[remainder] = True
			#print(f"memo: {memo}")
			return memo[remainder]
			
	memo[remainder] = False
	#print(f"memo: {memo}")
	return memo[remainder]
	
	
	
if __name__ == "__main__":
	numbers = [7,14]
	target = 700
	t1 = time.time()
	print(canSum(target, numbers))
	print(f"Time Required: {time.time() - t1}" )
	
	
#Write a function howSum(target, numbers) that takes in a targetSum and an array of integers as arguments

#The function should return an true if there exist a combination that adds up to the target and false if there is none