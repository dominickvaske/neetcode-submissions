class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_boats = 0
        people.sort()
        left, right = 0, len(people)-1

        while left <= right:
            leftP, rightP = people[left], people[right]

            if leftP + rightP <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            num_boats += 1
        
        return num_boats