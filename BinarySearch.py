from typing import List
'''
LC - https://leetcode.com/problems/binary-search/
Take 2 variables l and r for left and right and make the index 0 and the last value.
Find the middle index and check its value with the target each iteration. 
If the target greater than value change value of l from o to m + 1 index else change value of r to m - 1 index and continue iteration. 
The loop will while l <= r as we are ++ or --1 from m during each assignment if no more values to check l would become = or greater to r and we can stop the search. 
If not found after the loop return -1  
'''


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        l = 0  # Left index value
        m = 0  # Middle Value
        r = len(nums)-1  # Right index value
        while l <= r:
            m = l + ((r-1) // 2)  # Integer division to find the middle value
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1 
            else:
                l = m + 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    val = sol.binarySearch([-1,0,3,5,9,12], 2)
    if val == -1:
        print("Correct")
    val = sol.binarySearch([-1,0,3,5,9,12], 9)
    if val == 4:
        print("Correct")
