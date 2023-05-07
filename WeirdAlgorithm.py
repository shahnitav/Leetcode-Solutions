'''
Consider an algorithm that takes as input a positive integer n. If n
is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

https://cses.fi/problemset/task/1068

Input - 
1. Take in the input
2. Create a list and put the input as the first value
3. Make a infinite loop till the value of n is 1 
4. If n is even divide by two and if n is odd then multiply by 3 and add 1 and also append it to the list. 
5. Out of the loop return the list. 
'''

def weird_algorithm(n: int):
    # List
    weirdalgo = []
    weirdalgo.append(n)
    while n != 1:
        # If n is even
        if n%2 == 0:
            n = n//2 # Divide by 2
            weirdalgo.append(n)
        # If n is odd
        else:
            n = (n * 3) + 1 # Multiply by 3 and add 1
            weirdalgo.append(n)
    return weirdalgo

def main():
    # Input
    n = int(input())
    output = weird_algorithm(n)
    print(' '.join(str(x) for x in output))

if __name__ == '__main__':
    main()

    







