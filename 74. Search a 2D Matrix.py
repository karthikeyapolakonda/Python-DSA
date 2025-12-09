# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n - 1
        while l <= r:
            mid = (l+r)//2
            i = mid//n
            j = mid%n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r -= 1
            else:
                l += 1
        return False
