'''
CodeWars - https://www.codewars.com/kata/545cedaa9943f7fe7b000048
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

# My Solution 
import string

def is_pangram(s):
    '''
    Panagram
    - Every single letter of alphabet in the sentence >= 1 
    - Case Irrelevant 
    - Ignore Numbers and Punctuations 

    Steps - 
    1. Lower the case of the string
    2. Create a dictionary with a-z and value as 0
    3. Loop through the string and update the hashset only if the character isalpha() 
    4. In the end check if the value of the hashset has any 0 values if it has then return False Else Return True
    '''
    # Lower the case
    s_lower = s.lower()
    # Create a dictionary for lower case alphabets initialized with 0
    hash = dict.fromkeys(string.ascii_lowercase, 0)
    for i in s_lower:
        if i.isalpha():
            hash[i] = hash[i] + 1
    if 0 in hash.values():
        return False
    else:
        return True

# More efficient solutions
def is_pangram_set(s):
    return set(string.ascii_lowercase).issubset(s.lower())

def main():
    print("Should be True")
    print("The quick, brown fox jumps over the lazy dog!", is_pangram("The quick, brown fox jumps over the lazy dog!"))
    print("Should be False")
    print("1bcdefghijklmnopqrstuvwxyz", is_pangram("1bcdefghijklmnopqrstuvwxyz"))
if __name__ == '__main__':
    main()
