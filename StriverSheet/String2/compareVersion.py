def compareVersion(version1: str, version2: str) -> int:
    v1 = version1.split(".")
    v2 = version2.split(".")
    print(v1, v2)
    N1 = len(v1)
    N2 = len(v2)
    for i in range(max(N1, N2)):
        if i >= N1:
            n1 = 0
        else:
            n1 = int(v1[i])
        if i >= N2:
            n2 = 0
        else:
            n2 = int(v2[i])
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
    return 0

version1="1.0.1"
version2="1"
print(compareVersion(version1,version2))