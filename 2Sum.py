from typing import List
'''
    Need hashmap to store the remaining difference needed for each index
    index from 0 to len will check the difference betweeen target and value of index
    Add it two a hashmap based on the index. (As we are searching (int) a list would be easier to search through)
    Check if the new value is the required difference in the hashmap already otherwise add the different to the map.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = [] #Index of difference from the target
        for i,val in enumerate(nums):
            if val in hashmap:
                return [hashmap.index(val), i]
            else:
                diff =  target - val
                hashmap.append(diff)
        
if __name__ == "__main__":
    sol = Solution()
    val = sol.twoSum([2,7,11,15], 9)
    print(val)
    if val == [0,1]:
        print("True")
