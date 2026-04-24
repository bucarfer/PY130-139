'''1. Create a list where each number from the original list is squared using the map method.'''

l1 = [1, 2, 3, 4, 5]

def square_num(num):
    return num ** 2

nl1 = list(map(square_num, l1))
print(nl1)

## LS alternative solution, using a lambda function
nl1 = list(map(lambda x: x**2, l1))

'''2. Obtain only the even numbers from a list using the filter function.'''

l1 = [1, 2, 3, 4, 5]

nl1 = list(filter(lambda x: x%2 == 0, l1))
print(nl1)

'''3. Calculate the product of all numbers in a list using the reduce function.'''

from functools import reduce

l1 = [1, 2, 3, 4, 5]
new_list = reduce(lambda x, y: x*y, l1)
print(new_list) #120

#alternative with a function

def multiply(num1, num2):
    return num1 * num2

new_list = reduce(multiply, l1)

'''4. Use map to create a list of lengths of each string in the original list.'''ç

##Solution
l1 = ["apple", "dog", "Fernando"]

new_list = list(map(lambda x: len(x), l1))
print(list(new_list))

## LS use len directly (no need of a lambda function)
new_list = list(map(len, l1))

'''5. Use reduce to concatenate a list of strings into a single string.'''

from functools import reduce

l1 = ["apple", "dog", "Fernando"]

def add_words(word1, word2):
    return f"{word1} {word2}"

concatenate_list = reduce(add_words, l1)
print(concatenate_list)

## LS solution with a lambda function

from functools import reduce

l1 = ["apple", "dog", "Fernando"]

concatenate_list = reduce(lambda x, y: x + " " + y, l1)
print(concatenate_list)

'''6. Use nested generator expressions to create a flat list of numbers from a list of lists.'''


##Solution
list_of_lists = [[0, 1, 2], [3, 4, 5], [6]]
flat_list = list(item
                for sublist in list_of_lists
                for item in sublist)
print(flat_list) #[0, 1, 2, 3, 4, 5, 6]

##variation of the exercise when some items are not a list!!
list_of_lists = [[0, 1, 2], [3, 4, 5], 6]
flat_list = list(num
                for item in list_of_lists
                for num in (item if isinstance(item, list) else [item]))
print(flat_list)

'''7. Use a generator expression to yield each character of a string in reverse order.'''

word = "apple"
reversed_word = (word[i] for i in range(len(word) - 1, -1, -1))
for char in reversed_word:
    print(char)

'''8. Create a generator function that yields numbers from 1 to 5.'''

def yield_nums():
    for idx in range(1, 6):
        yield idx

for num in yield_nums():
    print(num)

'''9. Create a generator function that yields user input strings until the word "stop" is entered.'''

def generate_input():
    while True:
        my_input = input("enter your input: ")
        if my_input == "stop":
            break
        else:
            yield my_input

for word in generate_input():
    print(word)

'''10. Remove all None values from a list using the filter method.'''

l1 = [None, "APPLE", 2, [1, 2], None]

def check_none(item):
    return item != None
new_list = list(filter(check_none, l1))

## with lambda function

list_no_none = list(filter(lambda item: item is not None, l1))