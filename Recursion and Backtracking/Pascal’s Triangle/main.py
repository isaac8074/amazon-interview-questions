# Python3 program for Pascal's Triangle 
# A O(n^2) time and O(1) extra 
# space method for Pascal's Triangle 
  
# Pascal function 
def printPascal(n):

    for line in range(1, n + 1):
        C = 1 # used to represent C(line, i)
        for i in range(1, line + 1):

            # The first value in a 
            # line is always 1
            print(C, end = " ")
            C = int(C * (line - i) / i)
        print("")

# Driver code
n = 5
printPascal(n)