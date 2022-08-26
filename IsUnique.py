'''
isUnique - Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Create a hashmap with all the Unicode values and intialise them as False,
Iterate through the string and turn values to True and if character already true,
return False for the uniqueString
'''


class Solution:
    def isUnique(charString: str) -> bool:
        hashmap = [False for _ in range(128)] # ASCII Characterset intiialized
        for x in charString:
            val = ord(x)
            if hashmap[val]:
                return False
            else:
                hashmap[val] = True
        return True

if __name__ == "__main__":
        sol = Solution
        val = sol.isUnique("abcs")
        print(val)
        if val == True:
            print("Correct")