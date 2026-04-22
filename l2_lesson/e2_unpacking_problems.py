'''Practice Problem 1
Predict the output of the following code:'''

a, b, c = (1, 2, 3)
print(a, b, c)

# 1, 2, 3
# The code will output 1 2 3 since the values from the tuple are unpacked into the variables `a, b, c`

'''Practice Problem 2
What value will _ have after executing the following code?'''

a, _, c = (1, 2, 3)

# the variable `_` will have the second value from the tuple -> 2

'''Practice Problem 3
Will the following code raise an error? If so, what kind? Try answering without running the code.'''

a, b = (1, 2, 3)
# The number of variables do not match with the values of the tuple, it will raise a ValueError

'''Practice Problem 4
What happens when you run the following code? Try answering without running the code.'''

a, b, c, d, e = (1, 2, 3)
# Same, it will raise a ValueError since there are more variables than values to unpack

'''Practice Problem 5
What will rest contain after running this code? Try answering without running the code.'''

a, *rest = [1, 2, 3, 4, 5]
# the variable `rest` will contain the rest of the values in a list collection [2, 3, 4, 5]

'''Practice Problem 6
What will the following code output? Try answering without running the code.'''

first, *middle, last = "hello"
print(f"First: {first}, Middle: {middle}, Last: {last}")

#The string will be unpacked with first char for first, the middle characters for middle, and the last character for last
"First: h, Middle: ['e', 'l', 'l'], Last: o"

'''Practice Problem 7
Write a single line of code that swaps the values of a and b.'''

a = 1
b = 2
a, b = b, a
print(a, b)

'''Practice Problem 8
What will x and y be after this code runs?'''

((x, y), z) = ((1, 2), 3)

# This is a nested unpacking -> variable x = 1 and y = 2