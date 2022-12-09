def kthDistinct(arr: list[str], k: int) -> str:
    l = []
    for i in range(0, len(arr)):
        if arr.count(arr[i]) == 1:
            l.append(arr[i])
    if k > len(arr):
        print("hi")
        return ""
    elif len(arr) == k:
        print(arr[-1])
    else:
        print(arr[k - 1])


arr = ["d", "b", "c", "b", "c", "a"]
k = 2
# Output: "a"
kthDistinct(arr, k)
