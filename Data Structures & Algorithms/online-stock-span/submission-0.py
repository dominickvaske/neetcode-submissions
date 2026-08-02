class StockSpanner:

    def __init__(self):
        self.price_history = []

    def next(self, price: int) -> int:
        self.price_history.append(price)

        i = len(self.price_history) - 1
        span = 0
        while i >= 0 and self.price_history[i] <= price:
            i -= 1
            span += 1
        
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)