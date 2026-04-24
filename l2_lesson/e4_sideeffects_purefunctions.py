'''1. What side effects are present in the foo function in the following code?'''

bar = 42
qux = [1, 2, 3]
baz = 3

def foo(lst):
    value = lst.pop()
    print(f'popped {value} from the list')
    return value + bar + baz

foo(qux)

##Solution
# 1. mutates a variable outside the local scope -> qux
# 2. output to the console

'''2. Which of the following functions are pure functions?'''

def sum(a, b):
    print(a + b)
    return a + b

# it has a side effect (print), it is not pure

def sum(a, b):
    a + b

# it returns None always, but is is PURE

def sum(a, b):
    return a + b

# PURE FUNCTION, it returns a value that is based on the arguments

import random

def sum(a, b):
    return a + b + random.random()

# it uses random that will make the return change for the same argument, it is not

def sum(a, b):
    return 3.1415

# the return always the same value, but is PURE