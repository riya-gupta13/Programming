def decode(encoded: list[int], first: int) -> list[int]:
    l = [first] * (len(encoded) + 1)
    for i in range(1, len(l)):
        l[i] = encoded[i - 1] ^ l[i - 1]
    print(l)


encoded = [6,2,7,3]
first = 4
# Output: [1,0,2,1]
decode(encoded, first)
