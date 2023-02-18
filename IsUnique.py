'''
isUnique - Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Create a hashmap with all the Unicode values and intialise them as False,
Iterate through the string and turn values to True and if character already true,
return False for the uniqueString
'''
class Solution:
    # Check if the string is unique using a HashMap
    def isUnique(self, charString: str) -> bool:
        hashmap = [False for _ in range(128)] # ASCII Characterset intiialized
        for x in charString:
            val = ord(x)
            if hashmap[val]:
                return False
            else:
                hashmap[val] = True
        return True
    
    # Check if the string is unique using the Bit Vector Method
    def isStringUniqueBitVector(self, charString: str) -> bool:
        # Take a character check which starts as a an array of bits of 0
        charCheck = 0
        # Convert all character in string to lower so they fall in the same 26 character ASCII values
        charString = charString.lower()
        # Go through each character in the string
        for x in charString:
            i = ord(x) - ord('a') # Subtract the ASCII values character with a to find its index
            if ((charCheck & (1 << i)) > 0):
                return False
            else:
                charCheck = charCheck | i
        return True

if __name__ == "__main__":
        sol = Solution()
        print("HASHMAP METHOD - ")
        exp1 = "abcs"
        exp2 = "xuasda"
        print("Example - ", exp1, " Result - ", sol.isUnique(exp1))
        print("Example - ", exp2, " Result - ", sol.isUnique(exp2))
        print("BIT ARRAY METHOD - ")
        print("Example - ", exp1, " Result - ", sol.isStringUniqueBitVector(exp1))
        print("Example - ", exp2, " Result - ", sol.isStringUniqueBitVector(exp2))
