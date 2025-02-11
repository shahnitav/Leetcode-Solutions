'''
278. First Bad Version 

Binary search implementation - A good guide to follow - https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems
'''
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high = n
        low = 1
        while low<high:
            '''
            This is to handle overflow of numbers in sum languages like C & C++. The sum might be larger than the int value if you do (low + high ) // 2. 
            '''
            mid = low + (high - low) // 2
            if(isBadVersion(mid)):
                high = mid
            else:
                low = mid + 1
            return low
