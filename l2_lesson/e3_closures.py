'''1. What will the following code print?'''

def make_greeting():
    greeting = "Hello"

    def greet_func(name, greet=None): # closure
        if not greet:
            return f"{greeting} {name}!"

        return f"{greet} {name}!"

    return greet_func

greet_person = make_greeting() # holds a reference to the greet_func
print(greet_person("John", "Goodbye"))
print(greet_person("Jane"))

## Solution
# Goodbye John
# Hello Jane!

#IMP -> when we call make_greeting, it returns the function as an object, but it does not call the object, what it does it define the free variable greeting as "Hello"

'''2. What does the following program print? Try to answer without running the code:'''

def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

increment_counter = make_counter() #
print(increment_counter())
print(increment_counter())

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

## Solution
# 1
# 1
# 1
# 1
# Prints 1 four times, since counter is initialized to 0 every time we call the function

'''3. What will this code print? Try to answer without running the code:'''

from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

say_hello_to = partial(greet, greeting="Hello")
print(say_hello_to(name="Alice"))  # What will this print?

## SOlution
# Hello, Alice!
# With the partial function we create a new version of the function `greet` where we assigned the value "Hello" to the variable greeting,  when we call the function say_hello_to with the argument "Alice" assigned to the variable name and the prefilled variable greeting with the value "Hello"

'''4. Write a function named later that takes two arguments: a function, func, and an argument for that function, argument. The return value should be a new function that calls func with argument as its argument. Here's an example of how it might be used:'''

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
        # returns the define function inner but does not call it
print_warning()  # The system is shutting down! ## in this line is when we called the function

##Solution
def later(func, argument):
    def inner():
        return func(argument)
    return inner

'''5. Write a function named later2 that takes two arguments: a function, func, and an argument for that function, first_arg. The return value should be a new function that takes an argument, second_arg. The new function should call the func with the arguments provided by first_arg and second_arg. Here's an example of how it might be used:'''

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!

## Solution
def later2(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)

    return inner

