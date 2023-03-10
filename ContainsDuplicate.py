'''
217. Contains Duplicate - Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
from typing import List

class Solution():
    def containsDuplicate_Hashmap(self, nums: List[int]) -> bool:
        '''
        Check if the list contains duplicate using a Hashmap. We do not use an array/list here because to check if the key exist in list we have to go through each element individually but in a Hashmap/Dictionary/Set the algorithm has been optimized so this action can be performed in O(n).
        '''
        hashMap = {} # Empty dictionary
        for x in nums:
            if x not in hashMap:
                hashMap[x] = 1
            else:
                return True
        return False

    def containsDuplicate_Sort(self, nums: List[int]) -> bool:
        '''
        We will sort the values in a list and check if adjacent values are same or not. 
        '''
        nums.sort()
        for x in range(1, len(nums)):
            if nums[x] == nums[x-1]:
                return True
        return False

    def containsDuplicate_Set(self, nums: List[int]) -> bool:
        '''
        Set cannot contain duplicate values, so we will convert the list to set and then check the length of both and if there is a difference then there was a duplicate in the list. 
        '''
        return len(nums) != len(set(nums))

def main():
    sol = Solution()
    output = sol.containsDuplicate_Hashmap([1,1,1,3,3,4,3,2,4,2])
    print("Output with Hashmap - ", output)
    output = sol.containsDuplicate_Sort([1,1,1,3,3,4,3,2,4,2])
    print("Output with Sort - ", output)
    output = sol.containsDuplicate_Set([1,1,1,3,3,4,3,2,4,2])
    print("Output with Set - ", output)

if __name__ == '__main__':
    main()
