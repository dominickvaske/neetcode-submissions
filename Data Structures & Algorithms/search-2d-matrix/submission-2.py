class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = (l+r) // 2
            row = mid // COLS
            col = mid % COLS

            tmp = matrix[row][col]

            if tmp == target:
                return True
            elif tmp > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False