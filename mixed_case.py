"""
Problem:

    The function 'test_case' takes a string and should
    return whether that string is upper case, lower
    case or a mixture of upper and lower case 
    characters. It should print "Upper", "Lower" or
    "Mixed".


Tests:

    >>> test_case("a lower case string")
    Lower
    >>> test_case("AN UPPER CASE STRING")
    Upper
    >>> test_case("A mixed CASE string")
    Mixed
"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def test_case(s):

    if s == s.upper():
        print("Upper")

    elif s == s.lower():
        print("Lower")

    else:
        print("Mixed")
