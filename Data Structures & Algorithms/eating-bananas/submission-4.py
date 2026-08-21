class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #ans= float('inf')
        left=1
        right=-float('inf')
        subsum=0
        bestsum=0
        for p in piles:
            right=max(right, p)
        while left< right:
            mid=int((left+right)//2)
            subsum=0
            for pile in piles:
                subsum+=math.ceil(pile/mid)
            if subsum<=h:
                #ans=min(ans, mid)
                right=mid
            else:
                left=mid+1
        return left

        # maxnum=-float('inf')
        # result=float('inf')
        # for x in piles:
        #     maxnum=max(maxnum, x)
        # leftptr=1
        # rightptr=maxnum
        # while leftptr<=rightptr:
        #     mid=(leftptr+rightptr)//2
        #     sumpiles=0
        #     for x in piles:
        #         sumpiles=sumpiles+ math.ceil(x / mid)
        #     if sumpiles<=h:
        #         result=min(result, mid)
        #         rightptr=mid-1
        #     else:
        #         #result=min(result, sumpiles)
        #         leftptr=mid+1
        # return result