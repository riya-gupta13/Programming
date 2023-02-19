def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr


flatten([1, 2, 3, [4, 5]])
