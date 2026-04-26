class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left=0
        right = n*m-1
        while left<=right:
            mid = (left+right)//2
            if target==matrix[mid//n][mid%n]:
                return True
            elif target<matrix[mid//n][mid%n]:
                right=mid-1
            else:
                left=mid+1
        return False