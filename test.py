import unittest

class MyList:
    def process(self):
        return self

class TestMyList(unittest.TestCase):
    def test_process_returns_same_object(self):
        lst = MyList()
        self.assertIs(lst, lst.process())

unittest.main()