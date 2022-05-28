# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

def find_anagrams(str1, str2):
    # [insert your code here]
    return sorted(str1) == sorted(str2)

print(find_anagrams("listen", "car"))
