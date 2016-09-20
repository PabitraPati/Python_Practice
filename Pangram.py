'''
Program to check if the given string is a Pangram or not.

If a string contains all the alphabets (a to z) in it, it is said to be a Pangram.

Works for both Python 2.7 and Python 3.5

author - Pabitra Kumar Pati
'''

import string
from sys import version_info

def is_pangram(param):
    '''
    Takes a string as input.
    Returns True if the input string is a Pangram.
    Else returns False.
    '''
    # Removes the duplicate characters in the input
    s = set(list(param.strip()))
    # Remove white space in the string if any
    if ' ' in s:
        s.remove(' ')
    # Convert all the characters to lower case then sort and join them
    m = ''.join(sorted(set([i.lower() for i in s])))
    if version_info[0] < 3:
        ret = True if (m == string.lowercase) else False
    else:
        ret = True if (m == string.ascii_lowercase) else False

    return ret

param = str(input("Enter string to check pangram :-  "))
val = is_pangram(param)
if val:
    print("Given string is a pangram.")
else:
    print("Given string is not pangram.")
