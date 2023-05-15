'''
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

https://cses.fi/problemset/task/1069
'''
# Haven't practised Classes in a long time
class Repetitions:
    def __init__(self, s: str):
        self.s = s

    def repetitions(self):
        '''
        Sliding Window Problem where we have a left index and a right index. We go through the entire string and keep track of the letters with the maximum substring by subtracting the right index with the left index and seeing if the difference is greater than the value we had before till the right index reaches the end. 
        '''
        # If just one character return 1
        if len(self.s) == 1:
            return 1

        maxRep = 0 # Maximum Repetitions by a character
        l_index = 0
        r_index = 1
        rep = 0 # Temporary value of the current repetition
        while r_index < len(self.s):
            if self.s[l_index] != self.s[r_index]:
                rep = r_index-l_index
                maxRep = max(rep, maxRep)
                l_index = r_index 
            if ((r_index == len(self.s)-1) and (self.s[l_index] == self.s[r_index])):
                rep = r_index+1-l_index
                maxRep = max(rep, maxRep)
            r_index += 1
        return maxRep

def main():
    # Input from the user
    inp = str(input())
    sol = Repetitions(inp)
    print(sol.repetitions())
    
if __name__ == "__main__":
    main()
