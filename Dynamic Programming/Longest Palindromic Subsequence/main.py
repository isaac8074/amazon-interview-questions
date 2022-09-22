# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence
# in seq
 
dp = [[-1 for i in range(1001)]for j in range(1001)]
 
# Returns the length of the longest palindromic subsequence
# in seq
 
 
def lps(s1, s2, n1, n2):
 
    if (n1 == 0 or n2 == 0):
        return 0
 
    if (dp[n1][n2] != -1):
        return dp[n1][n2]
 
    if (s1[n1 - 1] == s2[n2 - 1]):
        dp[n1][n2] = 1 + lps(s1, s2, n1 - 1, n2 - 1)
        return dp[n1][n2]
    else:
        dp[n1][n2] = max(lps(s1, s2, n1 - 1, n2), lps(s1, s2, n1, n2 - 1))
        return dp[n1][n2]
 
# Driver program to test above functions
 
 
seq = "GEEKSFORGEEKS"
n = len(seq)
 
s2 = seq
s2 = s2[::-1]
print(f"The length of the LPS is {lps(s2, seq, n, n)}")
 
# This code is contributed by shinjanpatra