def calPoints(ops: list[str]) -> int:
    score = []
    for i in ops:
        if 'C' in i:
            score = score[:-1]
            print(score)
            continue
        if 'D' in i:
            score.append(int(score[-1]) * 2)
            print(score)
            continue
        if "+" in i:
            score.append(score[-2]+score[-1])
            print(score)
            continue
        if i.isnumeric() or int(i)<0:
            score.append(int(i))
            print(score)
    print(sum(score))


ops =["1"]
# Output: 30
calPoints(ops)
