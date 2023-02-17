def plusOne(self, digits: List[int]) -> List[int]:
    st = 1
    new = 0
    for i in digits[::-1]:
        new += st * i
        st *= 10
    e = new + 1
    ans = []
    for i in str(e):
        ans.append(int(i))
    return ans