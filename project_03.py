num = int(input('enter the number: '))


def make_negative(num):
    if num > 0:
        num *= -1
    else:
        pass
    return num


result = make_negative(num)

print(result)
