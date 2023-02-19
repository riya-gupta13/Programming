def largestAltitude(gain: list[int]) -> int:
    gain.insert(0, 0)
    print(gain)
    sum = 0
    l = []
    for i in gain:
        sum = sum + i
        l.append(sum)
    print(max(l))


gain = [-4, -3, -2, -1, 4, 3, 2]
# Output: 1
largestAltitude(gain)
