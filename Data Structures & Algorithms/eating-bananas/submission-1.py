class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxnum=-float('inf')
        result=float('inf')
        for x in piles:
            maxnum=max(maxnum, x)
        leftptr=1
        rightptr=maxnum
        while leftptr<=rightptr:
            mid=(leftptr+rightptr)//2
            sumpiles=0
            for x in piles:
                sumpiles=sumpiles+ math.ceil(x / mid)
            if sumpiles<=h:
                result=min(result, mid)
                rightptr=mid-1
            else:
                #result=min(result, sumpiles)
                leftptr=mid+1
        return result