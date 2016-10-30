"""
Problem:

    The function "find" takes in two strings as input, called
    word and s.  It should search for word in s.

    If s starts with word - print "Start"
    If s finished with word - print "End"
    If word is in the middle somewhere - print "Middle"
    If word does not appear anywhere- print "Not found"

    Word will only appear once in s.

    The search should be case-insensitive.

Tests:

    >>> find("Hell", "Hello world")
    Start
    >>> find("old", "If I were so bold")
    End
    >>> find("Over", "I would love some dover sole")
    Middle
    >>> find("Piece", "Peter piper picked a peck of pickled pepper")
    Not found

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
        doctest.testmod(verbose=True)


# Edit this code
def find(word, s):
        if s.startswith(word):
            print("Start")

        elif s.endswith(word.lower()):
            print("End")

        elif word.lower() in s.lower():
            print("Middle")

        else:
            print("Not found")


