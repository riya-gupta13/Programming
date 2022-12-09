def heightChecker(heights: list[int]) -> int:
    heightOrdered = sorted(heights)
    count = 0
    for i in range(0, len(heights)):
        if heights[i] != heightOrdered[i]:
            count += 1
    return count
