'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bae -> false
'''


class Solution():
    def oneAway(self, str1 : str, str2 : str) -> bool:
        '''
        Check the length of the 2 strings and see if there is a difference of one edit by inserting or deleting. If the length is same check the difference in the number of characters. 
        '''
        if abs(len(str1) - len(str2)) == 0:
            # If the length is same check the difference in character and if it is greater than one return False
            differences = self.findReplacement(str1, str2)
            if differences > 1:
                return False
            else:
                return True
        elif abs(len(str1) - len(str2)) == 1:
            differences = self.findDifferences(str1, str2)
            if differences > 1:
                return False
            else: 
                return True
        else: 
            return False

            
    def findReplacement(self, str1, str2) -> int:
        '''
        If both the strings are of the same length this functions finds number of characters that are different and returns the difference. 
        '''
        differences = 0 # Start the number of differences as 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                differences = differences + 1
        return differences
     
    def findDifferences(self, str1, str2) -> int:
        '''
        Find if the character difference between both the strings is just a single character or not. 
        '''
        differences = 0 # Start the number of difference in characters as 0 
        for i in str1:
            if i not in str2:
                differences = differences + 1
        return differences 

def main():
    sol = Solution()
    output = sol.oneAway('pale', 'bale')
    print("Output for 'pale, 'bale' should be true - ", output)
    output = sol.oneAway('pale', 'bae')
    print("Output for 'pale, 'bae' should be false - ", output)
if __name__ == '__main__':
    main()
