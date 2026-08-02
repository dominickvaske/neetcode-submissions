class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x:x[0])
        merged = []

        for start, end in intervals:
            if not merged:
                merged.append([start,end])
            else:
                p_start, p_end = merged[-1]

                if start <= p_end:
                    merged[-1][1] = max(p_end, end)
                else:
                    merged.append([start, end])
            
        return merged