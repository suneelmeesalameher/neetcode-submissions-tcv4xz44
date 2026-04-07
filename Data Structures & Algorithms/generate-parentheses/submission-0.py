class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        stack=[]
        def dfs(opencount, closecount):
            if opencount==closecount==n:
                result.append("".join(stack))
            if opencount<n:
                #can add
                stack.append("(")
                dfs(opencount+1,closecount)
                stack.pop()

            if closecount<opencount:
                #can add
                stack.append(")")
                dfs(opencount,closecount+1)
                stack.pop()
        dfs(0,0)
        return result
            
            