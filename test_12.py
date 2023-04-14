"""
Given an array of integers, return a new array with each value doubled.
"""


def maps(a):
    arr = []
    for num in a:
        num2 = num * 2
        arr.append(num2)
    print(arr)


maps([1, 2, 3])
