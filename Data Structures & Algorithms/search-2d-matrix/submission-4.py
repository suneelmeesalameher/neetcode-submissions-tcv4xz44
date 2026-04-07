class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        num = (row*col)-1
        
        left=0
        right=num

        while left<=right:
            mid=int((left+right)/2)
            midrow=(mid//col)
            midcol=(mid%col)
            if matrix[midrow][midcol]==target:
                return True
            if target>matrix[midrow][midcol]:
                left=mid+1
            if target<matrix[midrow][midcol]:
                right=mid-1
        return False

