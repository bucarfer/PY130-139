'''Boolean Assertions
Write a unittest assertion that will fail if value is not odd.'''

import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_odd(self):
        value = 3
        self.assertTrue(value%2 != 0, "value is not odd")

unittest.main()

'''Equality Assertions
Write a unittest assertion that will fail if value.lower() does not return 'xyz'.'''

import unittest

class TestSomething(unittest.TestCase):
    def test_value_lower_is_xyz(self):
        value = 'XYZ'
        self.assertEqual('xyz', value.lower())

unittest.main()

'''None Assertions
Write a unittest assertion that will fail if value is not None.'''

import unittest

class TestSomething(unittest.TestCase):
    def test_value_is_none(self):
        value = None
        self.assertIsNone(value)

unittest.main()

'''Included Object Assertions
Write a unittest assertion that will fail if the 'xyz' is not in the list lst.'''

import unittest

class TestSomething(unittest.TestCase):
    def test_xyz_in_lst(self):
        lst = ['abc', 'xyz']
        self.assertIn('xyz', lst)

unittest.main()

'''Not Included Object Assertions
Write a test that will fail if 'xyz' is one of the elements in the list lst.'''

import unittest

class TestSomething(unittest.TestCase):
    def test_xyz_not_in(self):
        lst = ["abc", "def"]
        self.assertNotIn("xyz", lst)

unittest.main()

'''Exception Assertions
Write a unittest assertion that will fail unless employee.hire() raises a NoExperienceError exception when an employee only has 2 years of experience.'''

class NoExperienceError(Exception):
    pass

class Employee:
    def __init__(self, experience):
        self.experience = experience
        self.hired = False

    def hire(self):
        if self.experience < 3:
            raise NoExperienceError
        else:
            self.hired = True

import unittest

class TestEmployee(unittest.TestCase):
    def test_hire_exception_with_low_experience(self):
        employee = Employee(2) # create instance object o Employee class with 2 years exp
        with self.assertRaises(NoExperienceError):
            employee.hire() # call hire method to raise the NoExperienceError

unittest.main()

'''Type Assertions
Write a unittest assertion that will fail if value is not an instance of the Numeric class or one of its subclasses.'''

import unittest

class Numeric:
    pass

class Integer(Numeric):
    pass

class TestNumeric(unittest.TestCase):
    def test_value_is_instance_of_numeric(self):
        value = Integer()
        self.assertIsInstance(value, Numeric)

unittest.main()

'''Same Object Assertions
Write a test that will fail if lst and the return value of lst.process are different objects.'''

import unittest

class MyList:
    def process(self):
        return self

class TestMyList(unittest.TestCase):
    def test_process_returns_same_object(self):
        lst = MyList()
        self.assertIs(lst, lst.process())

unittest.main()