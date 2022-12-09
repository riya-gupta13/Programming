def countGoodRectangles(rectangles: list[list[int]]) -> int:
    l=[]
    for i in rectangles:
        minimum= min(i)
        l.append(minimum)
    # print(max(l))
    maxLen= l.count(max(l))
    print(maxLen)


rectangles = [[2,3],[3,7],[4,3],[3,7]]
# Output: 3
countGoodRectangles(rectangles)