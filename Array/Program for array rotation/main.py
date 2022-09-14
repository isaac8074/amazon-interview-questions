# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d


def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

# UTILITY FUNCTIONS
# function to print an array


def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")

# Function to get gcd of a and b


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftRotate(arr, d, n)
printArray(arr, n)

# This code is contributed by Shreyanshi Arun
# Time Complexity: O(N)
# Space Complexity: O(1)
# steps:
# 1 3 5 7
# 3 5 7 1
# 3 2 5 4 7 6 1
# 2 4 6
# 4 6 2
# 3 4 5 6 7 1 2
