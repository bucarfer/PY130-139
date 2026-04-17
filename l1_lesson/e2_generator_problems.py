'''Question 1
Create a generator expression that generates the reciprocals of the numbers from 1 to 10. A reciprocal of a number n is 1 / n. Use a for loop to print each value.

'''

reciprocals_numbers = (1/num for num in range(1, 11))

for num in reciprocals_numbers:
    print(num)

'''Question 2
Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. Use a for loop to print each value.'''

def reciprocals(n):
    for value in range(1, n + 1):
        yield 1/value

for num in reciprocals(5):
    print(num)

#solution using a while loop inside the function
def reciprocals(n):
    num = 1
    while num <= n:
        yield 1/num
        num += 1

for num in reciprocals(5):
    print(num)

'''Question 3
Use a generator expression to capitalize every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.'''

str_list = ["cat", "dog", "fish"]

print(tuple(word.capitalize() for word in str_list))

'''Question 4
Create a generator function that generates the capitalized version of every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.

'''

str_list = ["cat", "dog", "fish"]

def capitalize(str_list):
    for word in str_list:
        yield word.capitalize()

print(tuple(capitalize(str_list)))

'''Question 5
Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. Use a single print invocation to print all the capitalized strings as a set.

'''

str_list = ["cat", "dog", "fish", "beast", "fernando"]

print(set(word.capitalize()
          for word in str_list
          if len(word) >= 5))

#{'Fernando', 'Beast'}

'''Question 6
Create a generator function that generates the capitalized version of every string in a list of strings whose length is less than 5. Use a single print invocation to print all the capitalized strings as a set.'''

str_list = ["cat", "dog", "fish", "beast", "fernando"]

def capitalized(words):
    for word in words:
        if len(word) < 5:
            yield word.capitalize()

print(set(capitalized(str_list)))
#{'Cat', 'Fish', 'Dog'}
