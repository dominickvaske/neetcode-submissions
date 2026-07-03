class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #dp = {} #hashmap of previously seen values, key: index i, value: total ways to get

        # def backtrack(i, currSum):
        #     if i == len(nums):
        #         return currSum == target # +1 way if currSum == target value, 0 otherwise
            
        #     return (backtrack(i+1, currSum + nums[i]) +
        #             backtrack(i+1, currSum - nums[i]))
        
        # return backtrack(0,0)

        dp = {} #key: (index, currSum), value: number of ways to get to target
        
        def memoization(i, currSum):
            if i == len(nums):
                return currSum == target
            
            if (i,currSum) in dp:
                return dp[(i,currSum)]
            
            dp[(i, currSum)] = (memoization(i+1, currSum + nums[i]) +
                     memoization(i+1, currSum - nums[i]))
            
            return dp[(i,currSum)]
            
        return memoization(0,0)
        

