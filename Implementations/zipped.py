s, o = map(int, input().split())
for x in zip(*[map(float, input().split()) for _ in range(o)]):
        print(sum(x)/o)