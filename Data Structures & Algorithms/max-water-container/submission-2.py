class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        left=0
        right = len(heights)-1
        while left<right:
            if heights[left]<heights[right]:
                base=right-left
                height=heights[left]
                area=base*height
                maxarea=max(area,maxarea)
                left+=1
            else:
                base=right-left
                height=heights[right]
                area=base*height
                maxarea=max(area,maxarea)
                right-=1
        return maxarea
