def nextGreatestLetter(letters: list[str], target: str) -> str:
    s = 0
    e = len(letters) - 1
    if target < letters[s] or target >= letters[e]:
        return letters[s]
    while s <= e:
        mid = (s + e) // 2
        # print(mid)
        if target < letters[mid]:
            e = mid - 1
        else:
            s = mid + 1
    return letters[s]


letters = ["x","x","y","y"]
target = "z"
# Output: "c"
print(nextGreatestLetter(letters, target))
