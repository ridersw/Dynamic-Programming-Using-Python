def canConstruct(target, wordBank, memo = {}):
	if target in memo:
		return memo[target]

	if target == "":
		return 1
		
	totalCount = 0	
	
	for word in wordBank:
		if word == target[:len(word)]:
			numWays = canConstruct(target[len(word):], wordBank, memo)
			totalCount += numWays
			
	
	memo[target] = totalCount
	return totalCount
	
	
if __name__ == "__main__":
	print(canConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
	print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
	print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
	print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
	print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
	"e", 
	"ee", 
	"eee", 
	"eeee", 
	"eeeee", 
	"eeeeee"]))