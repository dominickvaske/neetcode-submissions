class Leaderboard:

    def __init__(self):
        self.board = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        min_heap = []
        for player, score in self.board.items():
            heapq.heappush(min_heap, score)
            if len(min_heap) > K:
                heapq.heappop(min_heap)
        
        total = 0
        while min_heap:
            score = heapq.heappop(min_heap)
            total += score
        
        return total


    def reset(self, playerId: int) -> None:
        del self.board[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
