# Python3 program to find minimum
# number of characters to be
# removed to make two strings
# anagram.

# function to calculate minimum
# numbers of characters to be
# removed to make two strings anagram
def makeAnagram(a, b):
	buffer = [0] * 26
	for char in a:
		buffer[ord(char) - ord('a')] += 1
	for char in b:
		buffer[ord(char) - ord('a')] -= 1
	return sum(map(abs, buffer))

# Driver Code
if __name__ == "__main__" :

	str1 = "bcadeh"
	str2 = "hea"
	print(makeAnagram(str1, str2))
	
# This code is contributed
# by Raghib Ahsan
