'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
'''


def abbrev_name(name):
    arr = name.split(' ')
    arr2 = []
    for x in arr:
        arr2.append(x[:1].upper())

    return '.'.join(arr2)


abbrev_name('patrick feenan')
