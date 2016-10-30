"""
Problem:

    Generally, comparing numbers is very straightforward.
    Except when those numbers are stored as strings.
    Comparing two numbers written as strings compares them
    alphabetically, starting with the first digit of each.
    Hence, with strings, "2" > "11" because "2" > "1".

    The function 'compare' should take in two numbers,
    a and b, written as strings and should compare them,
    printing whichever is the biggest numerically.

    For the purposes of this problem, don't try to convert
    the strings to numbers.

    Hint: There will be no leading zeroes, so the length
    of the number should be useful in determining the size
    of each one.

Tests:

    >>> compare("7", "1")
    7
    >>> compare("15", "27")
    27
    >>> compare("173", "54")
    173
    >>> compare("92", "183")
    183
    >>> compare("12345", "12345")
    12345

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def compare(a, b):
    
    if len(a) == len(b):
        if a > b:
            print(a)

        else:
            print(b)

    elif len(a) < len(b):
        print(b)

    elif len(a) > len(b):
        print(a)

    else:
        print(a)

