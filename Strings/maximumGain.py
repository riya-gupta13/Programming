import re
def maximumGain(s: str, x: int, y: int) -> int:
    r = ['ab', 'ba']
    points=0
    # for i in r:
    if s.find(r[0])!=-1:
        points=points+x

            # print(points)
    print(points)



s = "aabbaaxybbaabb"
x = 4
y = 5
# Output: 19
maximumGain(s, x, y)