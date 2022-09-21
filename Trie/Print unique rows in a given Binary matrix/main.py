# Python3 code to print unique row in a
# given binary matrix
 
def printArray(matrix):
 
    rowCount = len(matrix)
    if rowCount == 0:
        return
 
    columnCount = len(matrix[0])
    if columnCount == 0:
        return
 
    row_output_format = " ".join(["%s"] * columnCount)
 
    printed = {}
 
    for row in matrix:
        routput = row_output_format % tuple(row)
        if routput not in printed:
            printed[routput] = True
            print(routput)
 
# Driver Code
mat = [[0, 1, 0, 0, 1],
       [1, 0, 1, 1, 0],
       [0, 1, 0, 0, 1],
       [1, 1, 1, 0, 0]]
 
printArray(mat)
 
# This code is contributed by myronwalker
# Time Complexity: O(ROW x Col) - To Traverse the matrix and insert in the HashSet 
# Space Complexity: O(Row) - to store the hashset O(Row x Col)