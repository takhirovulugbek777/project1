"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
"""


def digitize(n):
    arr = []
    n = str(n)
    for num in n:
        arr.append(int(num))
    print(arr[::-1])


digitize(1579)
