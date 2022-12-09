import collections


def repeatedNumbers(arr):
    d = collections.Counter(arr)
    return d

array=[1,1,2,2,3]
print(repeatedNumbers(array))