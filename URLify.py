'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
'''
class Solution():
    def __init__(self):
        pass

    def urlify(self, input: str) -> str:
        urlify_str = input.rstrip() # Remove all trailing whitespaces
        urlify_str = urlify_str.replace(' ', '%20') #Replace the remaining whitespaces with %20
        return urlify_str

def main():
    sol = Solution()
    output = sol.urlify('Mr John Smith    ')
    print(output)

if __name__ == "__main__":
    main()

