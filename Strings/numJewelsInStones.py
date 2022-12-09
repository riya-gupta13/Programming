def numJewelsInStones(jewels: str, stones: str) -> int:
    list_jewels = list(jewels)
    list_stones = list(stones)
    count = 0
    for j in list_jewels:
        for i in list_stones:
            if i == j:
                count = count + 1
    print(count)


jewels = "z"
stones = "ZzzZ"
# Output: 3
numJewelsInStones(jewels, stones)
