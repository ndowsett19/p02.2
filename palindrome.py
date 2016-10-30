"""
Problem:

    A palindrome is a word that is spelt the same forwards as it is
    backwards, such as "racecar" or "mum".

    The function 'is_palindrome' should test whether a word is a
    palindrome or not and print either "Palindrome" or "Non-palindrome"

    The function should be case-insensitive, so "Racecar" should still
    be counted as a palindrome.

Tests:

    >>> is_palindrome("racecar")
    Palindrome
    >>> is_palindrome("RaceCar")
    Palindrome
    >>> is_palindrome("AManAPlanACanalPanama")
    Palindrome
    >>> is_palindrome("Test")
    Non-palindrome
    >>> is_palindrome("Aloha")
    Non-palindrome

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def is_palindrome(word):
    if word.lower()[::-1] == word.lower():
        print("Palindrome")

    else:
        print("Non-palindrome")


