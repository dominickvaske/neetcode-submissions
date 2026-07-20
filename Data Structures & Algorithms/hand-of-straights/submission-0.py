class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = Counter(hand)
        min_heap = []
        heapq.heapify(min_heap)

        for element, count in counts.items():
            heapq.heappush(min_heap,(element,count))
        
        while min_heap:
            hold = []

            for _ in range(groupSize):
                if not min_heap:
                    return False

                element, count = heapq.heappop(min_heap)
                
                if hold and element != hold[-1][0] + 1:
                        return False
                
                hold.append((element, count-1))
            
            for i in range(len(hold)):
                if hold[i][1] > 0:
                    heapq.heappush(min_heap, hold[i])
        
        return True
