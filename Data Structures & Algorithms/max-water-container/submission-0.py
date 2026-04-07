class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first=0
        last=len(heights)-1
        base=len(heights)-1
        maxarea=0
        for i in range(0, len(heights)):
            if heights[first]>heights[last]:
                maxh=heights[last]
            else:
                maxh=heights[first]
            area= maxh*base
            if maxarea<area:
                maxarea=area
            if heights[first]<=heights[last]:
                first=first+1
                base=base-1
            else:
                last=last-1
                base=base-1
        return maxarea
            