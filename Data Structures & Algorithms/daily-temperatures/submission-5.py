class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stk=[]

        for i, temp in enumerate(temperatures):
            
            # les do append first
            if len(stk)>0 and temp< stk[-1][0]:
                stk.append([temp,i])
            elif len(stk)==0:
                stk.append([temp,i])
            
            # if temp>stk[-1]
            while len(stk)>0 and temp>stk[-1][0] :
                poptemp, popi = stk.pop()
                ans[popi]=i-popi
            
            stk.append([temp,i])
        return ans