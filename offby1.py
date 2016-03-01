'''
Created on Feb 29, 2016

@author: Miranda Motsinger

I have tested this code with the given test cases and it passes all of them.
I understand that misrepresenting passing test cases is an academic
integrity violation.

Determines if two strings match except for exactly one character insertion,
deletion, or replacement. More or less than one of these prints False, 
exactly one prints True. (e.g. "abc" and "abc" returns False, "strut" and
"stratt" returns False, "if" and "iff" returns True.)
'''

import sys


# Evaluates whether string_a is "off by 1" from string_b using the rules
# described in the header comment.
# It evaluates the strings based on their difference in length. If their
# lengths are 2 apart, they can't be off by 1; if their lengths are 1 apart,
# they need to match except for the extra char; and if their lengths are the
# same, they must have exactly one different char.
def offby1(string_a, string_b):

    # str_one's len always >= str_two's.
    if len(string_a) == len(string_b):
        str_one = string_a
        str_two = string_b
    else:
        str_one = max(string_a, string_b, key=len)
        str_two = min(string_a, string_b, key=len)

    if len(str_one) - len(str_two) > 1:  # diff. in length > 1 case
        return False

    # Diff. in length == 1 case. The first mismatched char is assumed to be
    # the "extra" char and is removed. If there's another mismatched char
    # after that, the strings are off by more than one.
    elif len(str_one) - len(str_two) == 1:
        for i in range(len(str_two)):
            if str_one[i] != str_two[i] and len(str_one) != len(str_two):
                str_one = str_one.replace(str_one[i], "", 1)  # first mismatch
            if str_one[i] != str_two[i] and len(str_one) == len(str_two):
                return False  # second mismatch

        return True

    elif len(str_one) == len(str_two):  # same length case
        mismatch_count = 0
        for i in range(len(str_one)):
            if str_one[i] != str_two[i]:
                mismatch_count += 1

        if mismatch_count == 1:
            return True
        else:
            return False


string_one, string_two = sys.stdin.readline(), sys.stdin.readline()

print(str(offby1(string_one, string_two)))