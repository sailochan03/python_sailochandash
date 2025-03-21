def iterative_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input('Enter n: '))
print(f'Sum of first {n} natural numbers is {iterative_sum(n)}')

'''
Time Complexity = O(n)

For loop is iterating for n time to access n numbers and adding it to sum variable. Hence, the maximum time this loop will continue is n, which makes the time complexity of this function as O(n).
'''