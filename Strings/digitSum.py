def digitSum(s: str, k: int) -> str:
    while len(s) > k:
        out = []
        y = k
        for i in range(0, len(s), y):
            st = s[i:y]
            y += k
            out.append(st)
        print(out)
        sum = ''
        for i in out:
            digit = 0
            for j in i:
                digit += int(j)
            sum += str(digit)
        s = sum
        print(s)


s = "11111222223"
k = 4
# Output: "135"
digitSum(s, k)
