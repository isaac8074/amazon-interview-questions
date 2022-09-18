# Python Program to print left view
 
# Tree Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# function to get the left view of binary tree
def leftView(root):
    ans = []
 
    if not root:
        return ans
 
    q = []
    q.append(root)
    q.append(None)
    ok = True
 
    while len(q) != 0:
        it = q[0]
        del q[0]
        if it == None:
            if ok == False:
                ok = True
            if len(q) == 0:
                break
 
            else:
                q.append(None)
 
        else:
            if ok:
                ans.append(it.data)
                ok = False
 
            if it.left != None:
                q.append(it.left)
            if it.right != None:
                q.append(it.right)
 
    return ans
 
 
# Driver Code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(8)
    root.right.right = Node(15)
    root.right.left = Node(12)
    root.right.right.left = Node(14)
 
    vec = leftView(root)
 
    # print the left view
    for x in vec:
        print(x, end=" ")
    print()
 
# This code is contributed by Tapesh(tapeshdua420)
'''
Time Complexity: O(n) - where n is the number of nodes in the binary tree
Space Complexity: O(n) - since using space for auxiliary queue
'''