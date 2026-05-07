'''Roman Numerals
Write some code that converts modern decimal numbers into their Roman number equivalents.

The Romans were a clever bunch. They conquered most of Europe and ruled it for hundreds of years. They invented concrete and straight roads and even bikinis. One thing they never discovered though was the number zero. This made writing and dating extensive histories of their exploits slightly more challenging, but the system of numbers they came up with is still in use today. For example the BBC uses Roman numerals to date their programmes.

The Romans wrote numbers using letters - I, V, X, L, C, D, M. Notice that these letters have lots of straight lines and are hence easy to hack into stone tablets.

There is no need to be able to convert numbers larger than about 3000. (The Romans themselves didn't tend to go any higher)

Wikipedia says: Modern Roman numerals ... are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero.

To see this in practice, consider the example of 1990. In Roman numerals, 1990 is MCMXC:

1000=M
900=CM
90=XC

2008 is written as MMVIII'''

'''P
-transform decimal numbers to their equivalent Roman number
E
1990
1000=M
900=CM
90=XCe

From test cases
class RomanNumeral(num)
instance method `to_roman()`
only strings, conversion of decimals not needed
R
-1st digit [I -1 , V - 5, ]
-2nd digit X - 10, L - 50,
-3rd digit C - 100, D - 500,
-4th digit M - 1000

- transcribe digit by digit, left to right (skip digits = 0)
- no need to transform numbers greater than 3000
-
D
use dictionary to transform digits to roman numbers
2n idea -> use 4 list -> one for each digit (seems more direct)
A
transform number to numeric string
build 4 lists for each digit

1 = ["I", "II", "III", "IV", "VI", "VII", "VIII", "IX"]
2 = ["X", "XX", "XXX", "XL", "LX", "LXX", "LXXX", "XL"]
3 = ["C", "CC", "CCC", "CD", "DC", "DCC", "DCCC", "CM"]
4 = ["M", "MM", "MMM"]

generic = [1: "a", 2: "aa", 3: "aaa", 4: "ab", 5: "b", 6: "ba", , 7: "baa", 8: "baaa", 9: "ac"]

C
'''

'''*** Written solution of what I did. This program defines a RomanNumeral class that converts an integer into its modern Roman numeral representation.

The class is initialized with a single integer, which is stored on the instance for later use. The main behavior is provided by the to_roman instance method, which returns the Roman numeral form of that stored integer as a string.

To perform the conversion, the class uses a collection that maps Roman numeral strings to their corresponding integer values. These mappings are ordered from the largest value to the smallest. This order matters because modern Roman numerals are built by taking as many of the largest possible values first, then moving down to smaller values.

Inside to_roman, I start with an empty string that will hold the final Roman numeral and a working copy of the original number. I then iterate through each (roman_symbol, value) pair in the mapping. For each pair, I determine how many times the current value “fits into” the remaining number. If it fits at least once, I append the Roman symbol that many times to the result string. I then subtract the total value I just added from the remaining number (using the remainder from the division).

I repeat this process for each entry in the mapping, gradually reducing the number to zero while building up the Roman numeral string. When the loop finishes, all of the original number has been accounted for, and the accumulated string is the correct Roman numeral representation, which is then returned from to_roman.'''


'''
First, I define a dictionary that maps each digit (0–9) to a pattern written with generic symbols (a, b, c) that represent “one”, “five”, and “ten” for that digit.
Then, for each digit position (ones, tens, hundreds, thousands), I have another dictionary that maps those generic symbols to the actual Roman letters for that position (e.g. in the ones place, a -> I, b -> V, c -> X; in the tens place, a -> X, b -> L, c -> C, etc).

Step by step usage:
1. Split the original number into its digits.
2. For each digit, starting from the right (ones):
    2.1 Look up the generic pattern from the first dictionary.
    2.2 Replace its generic symbols using the position-specific mapping.
    2.3 Append that result to a string that builds the final Roman numeral.'''

class RomanNumeral:
    DIGIT_PATTERNS = {1: "a", 2: "aa", 3: "aaa", 4: "ab", 5: "b", 6: "ba", 7: "baa", 8: "baaa", 9: "ac"}
    PLACE_SYMBOLS = {
        1: {"a": "I", "b": "V", "c": "X"}, #ones
        2: {"a": "X", "b": "L", "c": "C"}, #tens
        3: {"a": "C", "b": "D", "c": "M"}, #hundreds
        4: {"a": "M"} #thousands
    }

    def __init__(self, num):
        self.num = num

    def to_roman(self):
        num_string = str(self.num)
        roman_num = ""
        for idx, digit in enumerate(num_string):
            place = len(num_string) - idx # place: 1 = ones, 2 = tens, 3 = hundreds, 4 = thousands
            digit_roman = self.convert_digit(place, digit)
            roman_num += digit_roman

        return roman_num

    def convert_digit(self, place, digit):
        digit_int = int(digit)

        if digit_int == 0 or place not in self.PLACE_SYMBOLS:
            return ""

        value = self.DIGIT_PATTERNS[digit_int]
        mapping = self.PLACE_SYMBOLS[place]

        return "".join(mapping[char] for char in value) #important we cannot use `sum` with string

#LS solution

class RomanNumeral:
    def __init__(self, number):
        self.number = number

    ROMAN_NUMERALS = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def to_roman(self):
        roman_version = ""
        to_convert = self.number

        for key, value in self.__class__.ROMAN_NUMERALS.items():
            multiplier, remainder = divmod(to_convert, value)
            if multiplier > 0:
                roman_version += key * multiplier
            to_convert = remainder

        return roman_version

    #using divmod -> combination of // and %