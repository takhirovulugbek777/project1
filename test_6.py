'''
The first century spans from the year 1 up to and including the year 100,
 the second century - from the year 101 up to and including the year 200, etc.
'''


def century(year):
    if len(str(year)) < 4:
        return 1

    elif year % 100 == 0:
        num = str(year)
        a = int(num[:-2])
        return a

    else:
        num = str(year)
        a = int(num[:-2])
        return a + 1


result = century(89)

print(result)