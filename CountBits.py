'''
LeetCode - https://leetcode.com/problems/counting-bits/
Count number of 1 bits for a given number
'''
class Solution:
    def countBits(self, n: int) -> int:
        num_bits = 0
        while n:
            num_bits += n & 1
            n >>= 1
        return num_bits

if __name__ == "__main__":
    sol = Solution()
    val = sol.countBits(5)
    if val == 2:
        print("True")
    else:
        print("False")

    
