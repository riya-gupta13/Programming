def minPlatforms(arr, dep, n):
    arr = sorted(arr)
    dep = sorted(dep)
    plat_needed = 1
    result = 1
    i = 0
    j = 0

    while i <= n and j < n:
        if arr[i] <= dep[j]:
            plat_needed += 1
            i += 1
        elif arr[i] > dep[j]:
            plat_needed -= 1
            j += 1
        if result < plat_needed:
            result = plat_neededj
    return result


N = 2
arr = ['9:00', '9:45']
dep = ['9:20', '12:00']
print(minPlatforms(arr, dep, N))
