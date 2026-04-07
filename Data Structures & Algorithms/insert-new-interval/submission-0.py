class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[intervals[0]]
        for start, end in intervals:
            if start > ans[-1][1]:
                #---
                #.   ----
                ans.append([start, end])
            if start==ans[-1][1]:
                #---
                #. ---
                ans[-1][1]=end
            if start<ans[-1][1]:
                if end<ans[-1][1]:
                    #-----
                    # ---
                    pass
                else:
                    #---
                    # ---
                    ans[-1][1]=end
        return ans
        

