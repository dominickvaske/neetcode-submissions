class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # iterate across the asteroids, single pass
        for asteroid in asteroids:
            # append if right moving
            if asteroid > 0:
                stack.append(asteroid)
                continue
            
            alive = True
            # reflects left moving asteroid logic
            while stack and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop() # right asteroid explodes
                elif stack[-1] == abs(asteroid):
                    stack.pop() # right and left explode
                    alive = False
                    break
                else:
                    alive = False # just left explodes
                    break
            
            if alive and asteroid < 0:
                stack.append(asteroid)
        
        return stack

# [2 ]