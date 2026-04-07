class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #k_vals=[0]*(max(piles))
        
        totalcount=len(piles)
        left=1
        right=max(piles)
        while left<=right:
            mid=int((left+right)/2)
            count=0
            for pile in piles:
                count+=((pile+mid-1)//mid)

            if count<=h:
                right=mid-1
            if count>h:
                left=mid+1
            #totalcount=min(totalcount, count)

        return left
        

