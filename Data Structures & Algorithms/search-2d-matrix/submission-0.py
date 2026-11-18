class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # log(m) + log(N)

        # find the row index through binary search
        # find the column index through binary search

        # essentially, say you want to find 11
        # first, you find the row:
        # 

        left = 0
        right = len(matrix) - 1

        row = -1
        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                row = middle
                break
            elif matrix[middle][0] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            middle = (left + right) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
