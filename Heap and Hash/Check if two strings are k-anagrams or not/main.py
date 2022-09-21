# Python 3 program for the above approach
import sys
 
# Function to check k
# anagram of two strings
 
 
def kAnagrams(str1, str2, k):
 
    flag = 0
 
    list1 = []
 
    # First Condition: If both the
    # strings have different length ,
    # then they cannot form anagram
    if (len(str1) != len(str2)):
        sys.exit()
 
    # Converting str1 to Character Array arr1
    arr1 = list(str1)
 
    # Converting str2 to Character Array arr2
    arr2 = list(str2)
 
    # Sort arr1 in increasing order
    arr1.sort()
 
    # Sort arr2 in increasing order
    arr2.sort()
 
    # Iterate till str1.length()
    for i in range(len(str1)):
 
        # Condition if arr1[i] is
        # not equal to arr2[i]
        # then add it to list
        if (arr1[i] != arr2[i]):
            list1.append(arr2[i])
 
    # Condition to check if
    # strings for K-anagram or not
    if (len(list1) <= k):
        flag = 1
 
    if (flag == 1):
        return True
    else:
        return False
 
 
# Driver Code
if __name__ == "__main__":
 
    str1 = "fodr"
    str2 = "gork"
    k = 2
 
    # Function Call
    kAnagrams(str1, str2, k)
    if (kAnagrams(str1, str2, k) == True):
        print("Yes")
    else:
        print("No")