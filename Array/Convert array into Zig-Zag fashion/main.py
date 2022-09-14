def zigZag(arr, n):
    # use sort function to sort the array
    arr.sort()
    # traverse the array from 1 to n-1
    for i in range(1, n-1, 2):
        # swap value of current element with next element
        arr[i], arr[i+1] = arr[i+1], arr[i]
    # print the array
    print(arr)


# Driver program
if __name__ == "__main__":
    arr = [4, 3, 7, 8, 6, 2, 1]
    n = len(arr)
    zigZag(arr, n)
# 1 2 3 4 6 7 8
# 1
#     3
#   2
#         6
#       4
#            8
#          7
# Time Complexity: O(N*log(N)) because sorting is used
# Space Complexity: O(1)