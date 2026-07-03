class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        
        # Quick impossibility check
        if max(freq.values()) > (n + 1) // 2:
            return ""
        
        # Build a max-heap of (-count, char)
        heap = [(-count, ch) for ch, count in freq.items()]
        heapq.heapify(heap)
        
        result = []
        
        # While we have at least two characters to place
        while len(heap) >= 2:
            count1, ch1 = heapq.heappop(heap)  # most frequent
            count2, ch2 = heapq.heappop(heap)  # second most frequent
            
            # Append them in order
            result.append(ch1)
            result.append(ch2)
            
            # Increment counts (they are negative, so +1 moves toward zero)
            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, ch1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, ch2))
        
        # If one char is left, handle it
        if heap:
            count, ch = heapq.heappop(heap)
            # If count is -1, we can safely add one more
            if count == -1:
                # Just make sure it doesn't match the previous char
                if result and result[-1] == ch:
                    return ""
                result.append(ch)
            else:
                # More than one remaining -> impossible (shouldn't happen if we did the initial check)
                return ""
        
        return "".join(result)