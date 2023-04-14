"""Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive,
non-zero numbers."""


def is_divisible(n, x, y):
    if n % x == 0:
        if n % y == 0:
            return f'true because {n} is divisible by {x} and {y}'
        else:
            return f'false because {n} is not divisible by {y}'
    else:
        return f'false because {n} is not divisible by {x}'


result = is_divisible(100, 2, 6)
print(result)
