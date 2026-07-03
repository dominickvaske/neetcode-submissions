class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #variation of binary search
        n = len(matrix[0]) * len(matrix) #number of elements total
        mid = 0
        start = 0
        end = n-1

        while start <= end:

            mid = (start + end) // 2
            row = mid // len(matrix[0]) #how many full rows will fit into value
            col = mid % len(matrix[0]) #remainder tells you how far into row you are

            currNum = matrix[row][col]

            if currNum == target:
                return True
            elif currNum > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False