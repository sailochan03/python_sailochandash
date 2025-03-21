def josephus(n, k):
    if n == 1:      # base case
        return 0
    else:
        return (josephus(n - 1, k) + k) % n     # recursive step

n = int(input('Enter n: '))
k = int(input('Enter k: '))

print(f'The last standing person is {josephus(n, k)}')

'''
Explanation of the base case and recursive step.
-> Base case: When n is 1, means the last person remains with position 0
-> Recursive step: 
        -josephus(n - 1, k) gives the position of the survivor in a circle of n - 1 people.
        - We need to shift this position by k places because we are eliminating every k-th person.
        - The modulo operation % n ensures that the position wraps around the circle.

Time Complexity = O(n)
The function makes n recursive calls, which makes the time complexity O(n).
'''