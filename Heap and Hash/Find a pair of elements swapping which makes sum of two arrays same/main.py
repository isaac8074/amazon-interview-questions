# Python Code for the above approach
def findSwapValues(a, m, b, n):
 
    # initialize 2 dictionary. dictionary takes operations (i.e. search,
    # insert, delete) in O(1) time on an average.
    x, y = {}, {}
 
    s1, s2 = 0, 0
 
    # Determining sum s1 of the elements of array
    # a[], and simultaneously inserting the array in the dictionary x
    for i in range(m):
        s1 += a[i]
        x[a[i]] = x.get(a[i], 0) + 1
 
    # Determining sum s2 of the elements of array
    # b[], and simultaneously inserting the array in the dictionary y
    for i in range(n):
        s2 += b[i]
        y[b[i]] = y.get(b[i], 0) + 1
 
    if (s1 - s2) % 2:  # Checking if difference between the two arrays sums is even or not
        print("No such values exist.")
        return
 
    for p in x:
        q = ((s2 - s1)//2) + p
        if q in y:  # Finding q for a given p in O(1) time.
            print(p, q)
            return
    print("No such values exist.")
 
 
if __name__ == "__main__":
    a = [4, 1, 2, 1, 1, 2]
    b = [1, 6, 3, 3]
    m = len(a)
    n = len(b)
    findSwapValues(a, m, b, n)
# This Code is Contributed by Vivek Maddeshiya
'''
Time Complexity: O(m + n)
Space Complexity: O(s + t)
'''