class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)

        for i, num in enumerate(temperatures):
            if len(stack)>0:
                while len(stack)>0 and stack[-1][0]<num:
                    value= stack.pop()
                    ans[value[1]]=i-value[1]
                stack.append([num,i])
            else:
                stack.append([num,i])
        return ans
