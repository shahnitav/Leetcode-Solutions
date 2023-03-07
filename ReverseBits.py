'''
190. Reverse Bit - Reverse bits of a given 32 bits unsigned integer.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        Take the last bit of n using & with 1 and then XOR it with the left shift of Reverse number so it ( 0 XOR (last n bit) -> which will be equal to the bit itself) and set it as the reverse number. 
        '''
        rev = 0
        for i in range(32): # 32 bit number
            rev = (rev << 1 ) ^ (n & 1)
            n >>= 1 # Drop 1 bit from n
        return rev

def main():
    sol = Solution()
    print("n:00000010100101000001111010011100 \n expected: 964176192 \n r:", sol.reverseBits(00000010100101000001111010011100))

if __name__ == '__main__':
    main()

