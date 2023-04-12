'''
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).
'''


def count_sheeps(sheep):
    num = 0
    for item in sheep:
        if item == True:
            num = num + 1
    print(num)


count_sheeps([True, True, True, False,
              True, True, True, True,
              True, False, True, False,
              True, False, False, True,
              True, True, True, True,
              False, False, True, True])
