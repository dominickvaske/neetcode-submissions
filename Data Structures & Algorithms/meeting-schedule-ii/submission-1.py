"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        heapq.heapify(rooms)
        max_rooms = 0

        intervals = sorted(intervals, key=lambda x:x.start)

        for interval in intervals:
            start, end = interval.start, interval.end
            # look for all previous end times that end before
            # current start
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, end)
            max_rooms = max(max_rooms, len(rooms))
        
        return max_rooms