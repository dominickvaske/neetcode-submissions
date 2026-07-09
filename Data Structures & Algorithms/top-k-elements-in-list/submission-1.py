class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freqMap = defaultdict(int)

        # for num in nums:
        #     freqMap[num] += 1
        
        minHeap = [(count, num) for num, count in Counter(nums).items()]

        heapq.heapify(minHeap)

        # remove all items smaller than the k necessary
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        # now have the top k items, convert to list
        res = []
        while minHeap:
            _, num = heapq.heappop(minHeap)
            res.append(num)
        
        return res

