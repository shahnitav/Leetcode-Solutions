'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
'''
class Solution():
    def __init__(self):
        pass

    def checkpermutation(self, string1: str, string2: str) -> bool:
        '''
        Sort the strings and check if they are the same or not. Different cases are considered different. 
        '''
        if len(string1) != len(string2):
            return False
        return ''.join(sorted(string1)) == ''.join(sorted(string2)) 


def main():
    sol = Solution()
    val = sol.checkpermutation('abcd','cdba')
    print(val)

if __name__ == "__main__":
    main()
