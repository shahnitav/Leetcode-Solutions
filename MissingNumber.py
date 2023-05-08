'''
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

https://cses.fi/problemset/task/1083

1. Take n as input and find the sum of 1-n integers
2. Take the n-1 input from the user and find the sum of all of the numbers
3. Subtract it and print the number

'''
def missing_number():
    # Input of integer n
    n = int(input())
    sum_n = (n * (n+1))/2
    # Input of the list of n-1 numbers
    numbers_raw = input()
    # Parse the string into a list of numbers
    numbers = [int(x) for x in numbers_raw.split()]
    sum_numbers = sum(numbers)
    # Subtract total sum from the sum_numbers to find the missing number
    print(str(int(sum_n-sum_numbers)))

def main():
    missing_number()

if __name__ == '__main__':
    main()
