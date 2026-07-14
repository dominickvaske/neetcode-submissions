class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_passengers = 0
        min_heap = []
        heapq.heapify(min_heap)

        # sort the trips by start
        trips = sorted(trips, key=lambda x:x[1])

        for passengers, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                last_end, old_passengers = heapq.heappop(min_heap)
                curr_passengers -= old_passengers

            curr_passengers += passengers
            if curr_passengers > capacity:
                return False

            heapq.heappush(min_heap, [end, passengers])
        
        return True