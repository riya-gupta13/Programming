# Find the Second Largest number in the array without using sort

def ma(l):
    maximum = -1
    for i in l:
        if i > maximum:
            maximum = i
    return maximum


def secondLargest(l):
    first, sec = l[0], l[1]
    if first < sec:
        first, sec = sec, first
    for i in l[2:]:
        if i > first:
            first, sec = i, first
        elif i > sec:
            sec = i
    return sec


