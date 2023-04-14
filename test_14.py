"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
"""


def past(h, m, s):
    mh = h * 60 * 60 * 60
    mm = m * 60 * 60
    ms = s * 60
    return mh + mm + ms


result = past(0, 1, 1)
print(result)