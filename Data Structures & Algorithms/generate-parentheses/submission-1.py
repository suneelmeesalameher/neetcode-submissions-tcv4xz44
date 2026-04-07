class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        sublist=""
        open, close=0,0
        def dfs(open, close,n, sublist):
            if open<=n:
                # sublist+='('
                # open+=1
                dfs(open+1, close, n, sublist+'(')
            if close<=n:
                # sublist+=')'
                # close+=1
                if close<open:
                #if len(sublist)>0:
                    dfs(open,close+1,n, sublist+')')
            if open==close==n:
                res.append(sublist)
        dfs(open,close,n, sublist)
        return res