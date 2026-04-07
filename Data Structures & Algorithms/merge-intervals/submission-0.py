class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        i=0
        for start, end in intervals:
            if ans[-1][1]<start:
                ans.append([start, end]) #adding the non merging interval
            if ans[-1][1]==start:
                ans[-1][1]=end #updating the end of first one where start of second is the end of first
            if ans[-1][1]>start:
                if ans[-1][1]>end:
                    #case
                    #-----
                    # ---
                    pass
                else:
                    #case
                    #----
                    #.  ---
                    ans[-1][1]=end
        return ans