def recursive_sum(n):
    if n == 1:    # base case
        return n
    return n + recursive_sum(n - 1)     # recursive step

n = int(input('Enter n: '))
print(f'Sum of first {n} natural numbers is {recursive_sum(n)}')

'''
Time Complexity = O(n)

The function is calling itself by decrementing the argument value by 1, and it goes until the argument becomes 1. Hence n number of recursive call is called, which makes the time complexity of this function as O(n).
'''