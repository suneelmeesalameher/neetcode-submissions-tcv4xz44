class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans=[intervals[0]]
        for start, end in intervals:
            lastend=ans[-1][1]
            if start<=lastend:
                ans[-1][1]=max(lastend, end)
            else:
                ans.append([start, end])
        return ans