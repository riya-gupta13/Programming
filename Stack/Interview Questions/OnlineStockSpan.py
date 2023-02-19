# 901 leetcode
class StockSpanner:

    def __init__(self):
        # pair stack has [price,span]
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])
        return span
