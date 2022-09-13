'''
Leetcode - https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        f(n) - Number of ways to reach the top.
        f(1) - 1 Way
        f(2) - 2 Way to reach the top
        f(n) = f(n-1) + f(n-2)
        '''
        # Initialize the values of f(1) and f(2)
        f_n = 0 #f(n)
        n_1 = 2 #f(n-1)
        n_2 = 1 #f(n-2)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for _ in range(3,n+1):
                f_n = n_1 + n_2
                n_2 = n_1
                n_1 = f_n
            return f_n
    
if __name__ == '__main__':
    sol = Solution
    val = sol.climbStairs(None, 4)
    print(val)
    if val == 5:
        print("True")
    else:
        print("False")

                


