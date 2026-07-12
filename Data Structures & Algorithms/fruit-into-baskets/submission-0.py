class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        heldFruits = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(fruits)):
            # heldFruits.add(fruits[right])
            heldFruits[fruits[right]] += 1

            while len(heldFruits) > 2:
                heldFruits[fruits[left]] -= 1
                if heldFruits[fruits[left]] == 0:
                    del heldFruits[fruits[left]]
                left += 1
                
            ans = max(ans, right-left+1)
        
        return ans

                