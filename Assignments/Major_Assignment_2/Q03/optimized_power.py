def fast_power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half_power = fast_power(a, b // 2)
        return half_power * half_power
    else:
        return a * fast_power(a, b - 1)

a, b = int(input('Enter a: ')), int(input('Enter b: '))
print(f'{a} raised to the power {b} is {fast_power(a, b)}')

'''

Explanation of divide and conquer
    - The problem is divided into smaller subproblems by halving the exponent (b // 2).
    - The results of the subproblems are combined to solve the original problem.

Time Complexity = O(log b)
Each recursive call halves the exponent b, so it makes log2(b) recursive calls.

'''