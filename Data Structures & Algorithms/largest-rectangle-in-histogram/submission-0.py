class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0

        for i, height in enumerate(heights):
            if stack:
                start=i
                while stack and stack[-1][1]>height:
                    [idx, h]=stack.pop()
                    start=idx
                    area=(i-start)*h
                    maxarea=max(area, maxarea)
                    
                stack.append([start, height])
                
            else:
                stack.append([i,height])

        maxlen=len(heights)
        while stack:
            [i,height]=stack.pop()
            area=(maxlen-i)*height
            maxarea=max(area, maxarea)
        return maxarea