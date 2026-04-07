class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        leftptr=0
        rightptr=len(heights)-1
        while leftptr<rightptr:
            if heights[leftptr]<heights[rightptr]:
                height=heights[leftptr]
                base=abs(rightptr-leftptr)
                maxarea=max(maxarea, height*base)
                leftptr+=1
            else:
                height=heights[rightptr]
                base=abs(rightptr-leftptr)
                maxarea=max(maxarea, height*base)
                rightptr-=1
            
        
        return maxarea
