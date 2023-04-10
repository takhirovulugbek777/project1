def positive_sum(arr):
    new = 0

    for item in arr:
        if item > 0:
            new += item
        else:
            pass
    return new


arr = [1, -4, 7, 12]
sum_num = positive_sum(arr)
print(sum_num)