"""
7 KYU

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

LINK: https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

"""

def get_count(input_str):
    num_vowels = 0
    for e in input_str:
        if e == 'a' or e == 'e' or e == 'i' or e == 'o' or e == 'u':
            num_vowels += 1
    return num_vowels
  
  #BETTER SOLUTION
  
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
  
