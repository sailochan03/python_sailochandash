def josephus(n, k):
    position = 0
    for i in range(2, n + 1):
        position = (position + k) % i
    return position

n = int(input('Enter n: '))
k = int(input('Enter k: '))

print(f'The last standing person is {josephus(n, k)}')

'''
Time Complexity = O(n)
For loop continues for n time, which makes the time complexity O(n).
'''