# Python 3 program to check if a string
# is two time rotation of another string.

# Function to check if string2 is
# obtained by string 1
def isRotated(str1, str2):

    if (len(str1) != len(str2)):
        return False

    if (len(str1) < 2):
        return str1 == str2
    clock_rot = ""
    anticlock_rot = ""
    l = len(str2)

    # Initialize string as anti-clockwise rotation
    anticlock_rot = (anticlock_rot + str2[l - 2:] +
                     str2[0: l - 2])

    # Initialize string as clock wise rotation
    clock_rot = clock_rot + str2[2:] + str2[0:2]

    # check if any of them is equal to string1
    return (str1 == clock_rot or
            str1 == anticlock_rot)


# Driver code
if __name__ == "__main__":

    str1 = "geeks"
    str2 = "eksge"
if isRotated(str1, str2):
    print("Yes")
else:
    print("No")

# This code is contributed by ita_c
# Time complexity: O(n)
# Space Complexity: O(n)
