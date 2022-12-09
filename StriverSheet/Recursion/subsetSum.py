def subsetSumsHelper(ind, sum, arr, N, sumSubset):
    if ind == N:
        sumSubset.append(sum)
        return
    subsetSumsHelper(ind + 1, sum + arr.index(ind), arr, N, sumSubset)
    subsetSumsHelper(ind + 1, sum, arr, N, sumSubset)

    return sorted(sumSubset)
