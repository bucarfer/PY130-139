'''1. Create a function greet that takes three arguments: a name, a greeting, and a punctuation mark, with the punctuation defaulting to a period.'''

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good morning, Pete!

# Solution

def greet(name, greeting, p_mark='.'):
    return f"{greeting}, {name}{p_mark}"

'''2. Create a function create_user that takes a username and requires keyword-only arguments for email and age.'''

print(create_user("Srdjan", email="srdjan@example.com", age=39))
# {"username": "Srdjan", "email": "srdjan@example.com", "age": 39}
print(create_user("Srdjan", "srdjan@example.com", age=39))
# Raises an exception

## Solution

def create_user(username, *, email, age):
    return {"username": username, "email": email, "age": age}

'''3. Write a function build_profile that takes a first name and a last name, and any number of keyword arguments to add to a user's profile.'''

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}

## Solution, a key point is that **kwargs collects all the keyword arguments in a dictionary

def build_profile(name, lastname, **kwargs):
    profile_dict = {"first_name": name, "last_name": lastname}
    for key, value in kwargs.items():
        profile_dict[key] = value
    return profile_dict

'''4. Create a function concatenate that takes any number of strings and concatenates them into a single string with a space in between.'''

print(concatenate("Launch", "School", "is", "great")) # Launch School is great
print(concatenate("I", "am", "working", "on", "the", "PY130", "course")) # I am working on the PY130 course

## Solution
def concatenate(*args):
    final_str = ""
    for word in args:
        final_str += " " + word
    return final_str

##LS solution using join directly -> *args collects all the items in a tuple

def concatenate(*args):
    return " ".join(args)

'''5. Write a function display_info that takes a positional-only parameter data, and keyword-only parameters reverse and uppercase.'''

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC

## solution
def display_info(data, /, *, reverse=False, uppercase=False):
    if reverse:
        data = data[::-1]
    if uppercase:
        data = data.upper()
    return data

'''6. Given a list with four elements, unpack these elements into four separate variables.'''

lst = [10, 20, 30, 40]

a, b, c, d = lst

print(a)
print(b)
print(c)
print(d)

'''7. Unpack values from a tuple of four elements, but only keep the first and last values.'''

data = (100, 200, 300, 400)
a, *_, b = data

print(a)
print(b)
print(*_)

'''8. Unpack the first two elements from a list and store the remaining elements in another list.'''

numbers = [1, 2, 3, 4, 5, 6]
a, b, *rest = numbers

print(a)
print(b)
print(rest)

'''9. Given a nested tuple data = ((1, 2), (3, 4), (5, 6)), write some code to unpack this tuple into individual variables a, b, c, d, e, f.'''

nested_tuple = ((1, 2), (3, 4), (5, 6))

(a, b), (c, d), (e, f) = nested_tuple