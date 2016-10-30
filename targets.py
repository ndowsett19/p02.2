"""
Problem:

    We need to check whether a student has met or exceeded their
    target grade. Their target will be a grade "A-G" and the
    grade they achieved will be "A-G" or "U", with "A" being
    the best, and "G"/"U" the worst.

    The function 'on_track' takes in two inputs, target and grade.
    If a student has exceeded their target, it should print "Above target"
    If a student is on target, it should print, "On Target"
    If a student is below target, it should print "Below target".

    You can expect all grades to be uppercase (so no case checking/conversion
    is necessary).

Tests:

    >>> on_track("A", "B")
    Below Target
    >>> on_track("C", "B")
    Above Target
    >>> on_track("B", "D")
    Below Target
    >>> on_track("E", "A")
    Above Target
    >>> on_track("C", "C")
    On Target

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
        doctest.testmod(verbose=True)


# Edit this code
def on_track(target, grade):

        if target > grade:
            print("Above Target")

        elif target < grade:
            print("Below Target")

        else:
            print("On Target")

