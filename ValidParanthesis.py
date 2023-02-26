class Solution:
    def isValid(self, s: str) -> bool:
        '''
        If there are odd number of characters return False.
        If the stack is not empty match the character with the character onthe stack top and if they match pop them else append them. 
        If the stack is empty at the end return true
        '''
        if(len(s)%2 != 0 or len(s) == 0):
            return False
        else: 
            closingParanthesis = {'}': '{', ']': '[', ')': '('}
            stack = [] # Input Stack
            for x in s:
                if x in closingParanthesis:
                    if stack and stack[-1] == closingParanthesis[x]: #If the stack is not empty and the top value is a key of ClosingParanthesis that matches then pop the value and if it doesn't match then return False.
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(x)
            if stack:
                return False
            else: 
                return True

def main():
    sol = Solution()
    output = sol.isValid('{[]}')
    print("Output of {[]} should be True - ", output);

if __name__ == "__main__":
    main()
