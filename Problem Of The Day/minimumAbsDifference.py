def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    answer = []
    # Initialize minimum difference as a huge integer in order not
    # to miss the absolute difference of the first pair.
    min_pair_diff = float('inf')
    # Traverse the sorted array and calculate the minimum absolute difference.
    for i in range(len(arr) - 1):
        min_pair_diff = min(min_pair_diff, arr[i + 1] - arr[i])
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min_pair_diff:
            answer.append([arr[i], arr[i + 1]])
    print(answer)
    return answer


arr = [1,3,6,10,15]
# Output: [[1,2],[2,3],[3,4]]
minimumAbsDifference(arr)
