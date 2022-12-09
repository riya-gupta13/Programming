def heightChecker(heights: list[int]) -> int:
    heightOrdered = sorted(heights)
    count = 0
    print(heightOrdered)
    for i in range(0, len(heights)):
        if heights[i] != heightOrdered[i]:
            count += 1
    print(count)


heights = [1, 2, 3, 4, 5]
# Output: 3
heightChecker(heights)
