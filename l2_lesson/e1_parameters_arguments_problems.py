'''Practice Problem 1
Write a function named combine that takes three positional arguments and returns a tuple containing all three. Call this function with three different values.

'''

def combine(val1, val2, val3):
    return (val1, val2, val3)

print(combine(1, 2, "abc"))

'''Practice Problem 2
Define a function named multiply that accepts two positional-only arguments and returns their product. The function should not allow these parameters to be passed as keyword arguments.'''

def multiply(num1, num2, /):
    return num1 * num2

print(multiply(2, 3))
print(multiply(1, num2=5))

'''Practice Problem 3
Create a function named describe_pet that takes one positional argument animal_type and one keyword argument name with a default value of an empty string. The function should print a description of the pet. The function should not accept more than 1 positional argument.'''

def describe_pet(animal_type, *, name=""):
    print(f"the {animal_type} has {name} as a name")

describe_pet("dog", name="Rex")
describe_pet("dog", "Rex")

'''Practice Problem 4
Write a function named calculate_average that accepts any number of numeric arguments and returns their average. Make sure it returns None if no arguments are provided.'''

def calculate_average(*nums):
    if nums:
        return sum(nums)/ len(nums)
    else:
        None

print(calculate_average(2, 3, 5))
print(calculate_average())

# LS solution with one liner
def calculate_average(*args):
    return sum(args)/len(args) if args else None

'''Practice Problem 5
Create a function named find_person that accepts any number of keyword arguments in which each key is someone's name and the value is their associated profession. The function should check whether any of the key/value pairs has a key of "Antonina" and then, if the key is found, print a message that shows Antonina's profession. Otherwise, it should say "Antonina not found". The function should not accept any positional arguments.'''

def find_person(**kwargs):
    if "Antonina" in kwargs:
        print(f"{kwargs['Antonina']}")
    else:
        print("Antonina not found")

find_person("Antonina", "Bob") # takes 0 positional arguments
find_person(John="senior TA", Antonina="TA")
find_person(John="senior TA")

'''Practice Problem 6
Define a function named concat_strings that takes any number of strings and returns the concatenation of all the strings. Add a keyword-only argument sep with a default value of ' ' that specifies the separator to use between the strings.'''

def concat_strings(*strings, sep=" "): #IMPORTANT -> after *args they are all kwargs
    return sep.join(strings)

print(concat_strings("Pepa", "Pepe", "Pepita"))
print(concat_strings("Pepa", "Pepe", "Pepita", sep="-"))

'''Practice Problem 7
Create a function named register that takes exactly three arguments: username as positional-only, password as keyword-only, and age as either a positional or keyword argument. It should return a dictionary that includes username, password, and age keys with the values passed to the the function.

'''

def register(username, /, age, *, password):
    return {"username": username, "password": password, "age": age,}

print(register("antonio", 26, password="12345"))
print(register("antonio", age=26, password=12345))

'''Practice Problem 8
Create a function named print_message that requires a keyword-only argument (message) and an optional keyword-only argument (level) with a default value of "INFO". The function should print out the message prefixed with the level. The function shouldn't accept any positional arguments.

'''

def print_message( *, message, level="INFO",):
    print(f"{level} {message}")

print_message(message="estamos locos??")
print_message(level="FYI", message="estamos locos??")
# print_message("***", message="estamos locos??") #TyperError, takes 0 positional arguments, keyworkd only arguments