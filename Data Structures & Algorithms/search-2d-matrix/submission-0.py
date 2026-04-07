class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row= len(matrix)
        col=len(matrix[0])
        print(row)
        print(col)
        first=0
        last=row*col-1
        while first<=last:
            mid=int((first+last)//2)
            row1=int(mid//col)
            col1=int(mid%col)
            if matrix[row1][col1]==target:
                return True
            if matrix[row1][col1]< target:
                first=mid+1
            if matrix[row1][col1]> target:
                last=mid-1
        return False