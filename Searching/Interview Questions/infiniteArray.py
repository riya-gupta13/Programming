def infiniteArray(arr, target, start, end):
    # first find range
    # lets take box of 2 as array size
    start = 0
    end = 1

    #     condition for target to lue in range
    while start <= end:
        if target > arr[end]:
            # this is my new start
            temp = end + 1
            # if target dsnt lies here double the box size
            # end=end+previousSize *2
            end = end + (end - (start - 1)) * 2
            start = temp
    while start <= end:
        mid = (start + end) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid
    return -1
