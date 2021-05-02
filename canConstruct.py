def canConstruct(target, wordBank, memo = {}):

	if target in memo: return memo[target]
	
	if target == "": return True
		
	for word in wordBank:
		if word == target[:len(word)]:
			suffix = target[len(word):]
			if canConstruct(suffix, wordBank, memo) == True:
				memo[target] = True
				return True
	
	
	memo[target] = False			
	return False
	
if __name__ == "__main__":
	print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
	print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
	print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
	print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
	"e", 
	"ee", 
	"eee", 
	"eeee", 
	"eeeee", 
	"eeeeeef"]))