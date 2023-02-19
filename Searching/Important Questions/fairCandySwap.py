def fairCandySwap(aliceSizes: list[int], bobSizes: list[int]):
    sumA = sum(aliceSizes)
    sumB = sum(bobSizes)
    res = []
    for i in range(len(aliceSizes) - 1, -1, -1):
        for j in range(len(bobSizes) - 1, -1, -1):
            diff = aliceSizes[i] - bobSizes[j]
            if sumA - diff == sumB + diff:
                res.append(aliceSizes[i])
                res.append(bobSizes[j])
                return res
    return res
