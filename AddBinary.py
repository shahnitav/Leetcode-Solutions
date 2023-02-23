'''
Add Binary -
Given two binary strings a and b, return their sum as a binary string.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert binary string to int and add them and then return the binary string
        return bin(int(a,2) + int(b,2))[2:]

def main():
    sol = Solution()
    output = sol.addBinary('1010', '1011')
    print("Output of this addition should be - 10101, the output is - ", output)

if __name__ == "__main__":
    main()
