# Python3 effective program to
# shuffle an array of size 2n
 
# Function to shuffle an array of size 2n
def shufleArray(a, f, l):
 
    if (f > l):
        return
 
    # If only 2 element, return
    if (l - f == 1):
        return
 
    # Finding mid to divide the array
    mid = int((f + l) / 2)
 
    # Using temp for swapping first
    # half of the second array
    temp = mid + 1
 
    # Mid is use for swapping second
    # half for first array
    mmid = int((f + mid) / 2)
 
    # Swapping the element
    for i in range(mmid + 1, mid + 1):
        (a[i], a[temp]) = (a[temp], a[i])
        temp += 1
 
    # Recursively doing for first
    # half and second half
    shufleArray(a, f, mid)
    shufleArray(a, mid + 1, l)
 
 
# Driver Code
a = [1, 3, 5, 7, 2, 4, 6, 8]
n = len(a)
shufleArray(a, 0, n - 1)
 
for i in range(0, n):
    print(a[i], end = " ")
 
# This code is contributed by Smitha Dinesh Semwal