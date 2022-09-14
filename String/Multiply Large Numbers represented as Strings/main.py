# Python3 program to implement the above approach

# function to reverse the string
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


num1 = "1235421415454545454545454544"
tempnum1 = num1
num2 = "1714546546546545454544548544544545"
tempnum2 = num2

# Check condition if one string is negative
if (num1[0] == '-' and num2[0] != '-'):
    num1 = num1[1:]
elif (num1[0] != '-' and num2[0] == '-'):
    num2 = num2[1:]
elif (num1[0] == '-' and num2[0] == '-'):
    num1 = num1[1:]
    num2 = num2[1:]

s1 = num1
s2 = num2
s1 = reverse(s1)
s2 = reverse(s2)
m = [0]*(len(s1)+len(s2))

# Go from right to left in num1
for i in range(len(s1)):

    # Go from right to left in num2
    for j in range(len(s2)):
        m[i + j] = m[i + j] + (ord(s1[i]) - 48) * (ord(s2[j]) - 48)


product = ""
# Multiply with current digit of first number
# and add result to previously stored product
# at current position.
for i in range(len(m)):
    digit = m[i] % 10
    carry = m[i] // 10
    if (i + 1 < len(m)):
        m[i + 1] = m[i + 1] + carry
    product = str(digit) + product

# ignore '0's from the right
while (len(product) > 1 and product[0] == '0'):
    product = product[1:]

# check condition if one string is negative
if (tempnum1[0] == '-' and tempnum2[0] != '-'):
    product = "-" + product

elif (tempnum1[0] != '-' and tempnum2[0] == '-'):
    product = "-" + product


print("Product of the two numbers is :")
print(product)


# This code is contributed by Abhijeet Kumar(abhijeet19403)
# Time Complexity: O(m*n)
# Space Complexity: O(m+n)
