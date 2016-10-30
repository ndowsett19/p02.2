"""
Problem:

    Elton John is holding a party for a small selection of his many friends.
    Unfortunately, word of this has got round and lots of other people are
    trying to gatecrash.

    Elton has had to employ a bouncer to check whether people are on the
    guest list or not. The last two people to arrive are Elizabeth Hurley
    and Victoria Beckham.

    The function guestlist takes a name (a string). If it is either 
    "Elizabeth Hurley" or "Victoria Beckham", it should print "Come on in",
    otherwise it should print "You're not on the list - scram!"

Tests:

    >>> guestlist("Victoria Beckham")
    Come on in!
    >>> guestlist("Elizabeth Hurley")
    Come on in!
    >>> guestlist("Donald Trump")
    You're not on the list - scram!
    >>> guestlist("Tom Cruise")
    You're not on the list - scram!

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def guestlist(name):
    if name == "Victoria Beckham" or name == "Elizabeth Hurley":
        print("Come on in!")

    else:
        print("You're not on the list - scram!")
