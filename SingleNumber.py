'''
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
NOTE: Your algorithm should have a linear runtime complexity.

Input
A = [1, 2, 2, 3, 1]

Output
3

Input
A = [1, 2, 2]

Output
1
'''

array = list(map(int, input().strip().split()))
result = 0

for i in range(len(array)):
    result ^= array[i]
    print (result)