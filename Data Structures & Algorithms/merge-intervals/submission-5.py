class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[intervals[0]]
        for start, end in intervals:
            lastend=ans[-1][1]
            if start<=lastend:
                ans[-1][1]=max(lastend, end)
            else:
                ans.append([start,end])
        return ans

                

