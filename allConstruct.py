def allConstruct(target, wordBank):

	if target == "":
		return [[]]
		
	result = []	
	
	for word in wordBank:
		if word == target[:len(word)]:
			suffixWays = allConstruct(target[len(word):], wordBank)
			targetWays = [[word] + suff for suff in suffixWays]
			
			result.extend(targetWays)
			
	return result
	
if __name__ == "__main__":
	print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
	print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
	print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
	print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
	print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
	"e", 
	"ee", 
	"eee", 
	"eeee", 
	"eeeee", 
	"eeeeee"]))