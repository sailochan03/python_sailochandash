def power(a, b):
    ans = 1
    while b > 0:
        if b % 2 == 1:
            ans *= a
        a *= a
        b //= 2
    return ans

a, b = int(input('Enter a: ')), int(input('Enter b: '))
print(f'{a} raised to the power {b} is {power(a, b)}')