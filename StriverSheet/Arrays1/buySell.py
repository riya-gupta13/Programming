def maxProfitOptimal(prices: list[int]):
    max = 0
    min=float('inf')
    for i in range(0, len(prices)):
        if prices[i]<min:
            min=prices[i]
        profit = prices[i] - min
        if profit > max:
            max = profit
    return(max)


def maxProfit(prices: list[int]):
    max = float('-inf')
    profit = 0
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max:
                max = profit
    if max <= 0:
        return 0
    return(max)


prices = [7,1,5,3,6,4]
print(maxProfitOptimal(prices))
