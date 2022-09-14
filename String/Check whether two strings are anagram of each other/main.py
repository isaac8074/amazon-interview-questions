# Python program to check if two strings
# are anagrams of each other

NO_OF_CHARS = 256

# function to check if two strings
# are anagrams of each other
def areAnagram(str1,str2):
	
	# If both strings are of different
	# length. Removing this condition
	# will make the program fail for
	# strings like "aaca" and "aca"
	if(len(str1) != len(str2)):
		return False;
	
	# Create a count array and initialize
	# all values as 0
	count=[0 for i in range(NO_OF_CHARS)]
	i=0
	
	# For each character in input strings,
	# increment count in the corresponding
	# count array
	for i in range(len(str1)):
		count[ord(str1[i]) - ord('a')] += 1;
		count[ord(str2[i]) - ord('a')] -= 1;
		
	# See if there is any non-zero
	# value in count array
	for i in range(NO_OF_CHARS):
		if (count[i] != 0):
			return False
		
	
	return True

# Driver code
str1="geeksforgeeks"
str2="forgeeksgeeks"

# Function call
if (areAnagram(str1, str2)):
	print("The two strings are anagram of each other")
else:
	print("The two strings are not anagram of each other")
	
	
# This code is contributed by patel2127
# Time Complexity: O(n)
# Space Complexity: O(1)
