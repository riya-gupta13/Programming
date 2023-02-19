def smallestLetter(letters, target):
    s = 0
    e = len(letters) - 1
    while s <= e:
        mid = (s + e) // 2
        # print(mid)
        if target < letters[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return letters[s % len(letters)]


arr = ["x", "x", "y", "y"]
target = "z"
print(smallestLetter(arr, target))
