def basic_op(operator, value1, value2):
    # print(f'{value1}{operator}{value2}')
    if operator == '/':
        num = value1 / value2
    elif operator == '*':
        num = value1 * value2
    elif operator == '+':
        num = value1 + value2
    else:
        num = value1 - value2
    print(num)

basic_op('/', 49, 7)
