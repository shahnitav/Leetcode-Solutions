from typing import List
'''
    LC - https://leetcode.com/problems/single-number/
    Pass through the nums list once
    While going through it push the values on a stack
    Check if the value is already on the stack then remove it 
    The last remaining value will be the single number
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = [] # Push and pop the values to get the single number
        for val in nums:
            if val in stack:
                stack.remove(val)
            else:
                stack.append(val)
        return stack[0] # The last remaining value is the single number


if __name__ == "__main__":
    sol = Solution()
    val = sol.singleNumber([4,1,2,1,2])
    print(val)
    if val == 4:
        print("True")

'''
Neetcode solution with Bit Manipulation (Faster and less memory)
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
'''