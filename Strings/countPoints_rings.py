def countPoints(rings: str) -> int:
    count=0
    for i in range(10):
        if 'R' + str(i) in rings and 'G' + str(i) in rings and 'B' + str(i) in rings:
            count=count+1
    print(count)

    # print(sum([1 for i in range(10) if 'R' + str(i) in rings and 'G' + str(i) in rings and 'B' + str(i) in rings]))
    # return sum([i for i in range(10) if 'R' + str(i) in rings and 'G' + str(i) in rings and 'B' + str(i) in rings])

rings = "B0R0G0R9R0B0G0"
# Output: 1
countPoints(rings)
