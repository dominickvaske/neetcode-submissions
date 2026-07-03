class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        diff = [gas[i] - cost[i] for i in range(len(gas))]

        startingIdx = 0
        currTotal = 0
        while startingIdx < len(diff):
            i = startingIdx
            currTotal = 0

            while currTotal >= 0:
                currTotal += diff[i]
                i += 1
                if currTotal < 0:
                    break
                elif i == len(diff):
                    return startingIdx

            startingIdx += 1
        
        return -1






