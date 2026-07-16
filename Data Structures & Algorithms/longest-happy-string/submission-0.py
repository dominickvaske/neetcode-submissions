class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            max_heap.append([a,"a"])
        if b > 0:
            max_heap.append([b,"b"])
        if c > 0:
            max_heap.append([c,"c"])
        
        heapq.heapify_max(max_heap)
        output = []
        
        while max_heap:
            count, current_char = heapq.heappop_max(max_heap)

            if len(output) >= 2 and output[-2] == output[-1] == current_char:
                if max_heap:
                    count2, nxt_highest = heapq.heappop_max(max_heap)
                    output.append(nxt_highest)

                    if count2-1 > 0:
                        heapq.heappush_max(max_heap, [count2-1, nxt_highest])
                else:
                    return "".join(output)
            
            output.append(current_char)

            if count-1 > 0:
                heapq.heappush_max(max_heap, [count-1, current_char])
        
        return "".join(output)
            

            

