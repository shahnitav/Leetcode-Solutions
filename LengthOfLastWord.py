'''
Length of Last Word - Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal 
substring consisting of non-space characters only.
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string and return the length of the last word
        str_split = s.split()
        return len(str_split[-1])


def main():
    sol = Solution()
    output = sol.lengthOfLastWord("   fly me   to   the moon")
    print("The length of the last word should be 4 and it is - ", output)

if __name__ == "__main__":
    main()
