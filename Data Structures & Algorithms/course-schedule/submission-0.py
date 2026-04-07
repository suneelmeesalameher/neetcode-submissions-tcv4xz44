class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mydir={}
        visitset=set()
        for i in range(numCourses):
            mydir[i]=[]
        for cr, pr in prerequisites:
            mydir[cr].append(pr)
        
        def dfs(cr):
            if cr in visitset:
                return False
            if mydir[cr]==[]:
                return True

            visitset.add(cr)
            for pr in mydir[cr]:
                if not dfs(pr):
                    return False
            visitset.remove(cr)
            mydir[cr]=[]
            return True

        for cr in range(numCourses):
            if not dfs(cr):
                return False
        return True