def finalPrices(prices: list[int]) -> list[int]:
    for i in range(0, len(prices)):
        for j in range(0, len(prices)):
            if j > i and prices[j] <= prices[i]:
                print(prices[i], prices[j])
                prices[i] = prices[i] - prices[j]
                break

    print(prices)


prices =  [10,1,1,6]
# Output: [4,2,4,2,3]
finalPrices(prices)
