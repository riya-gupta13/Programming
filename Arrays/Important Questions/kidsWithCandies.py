def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    result = []
    for i in candies:
        greatest = i + extraCandies
        if greatest >= max(candies):
            result.append(True)
        else:
            result.append(False)
    print(result)
    return result


candies = [2, 3, 5, 1, 3]
extraCandies = 3
# [true,false,true]
kidsWithCandies(candies, extraCandies)
