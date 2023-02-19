def maxDistance(colors: list[int]) -> int:
    max = 0
    for i in range(0, len(colors)):
        for j in range(0,len(colors)):
            if colors[i] != colors[j] and i!=j:
                dis = abs(i - j)
                if max <= dis:
                    max = dis
    print(max)


colors = [0,1]
# Output: 4
maxDistance(colors)
