class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxarea=0

        while left<right:
            if heights[right] > heights[left]:
                maxh=heights[left]
            else:
                maxh=heights[right]
            area= (right-left)* maxh
            maxarea=max(maxarea, area)

            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return maxarea

            