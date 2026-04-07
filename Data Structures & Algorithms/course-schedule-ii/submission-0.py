class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        top=[]
        visit, cycle=set(), set()
        mydir={}
        for i in range(numCourses):
            mydir[i]=[]
        for cr, pr in prerequisites:
            mydir[cr].append(pr)

        def dfs(cr):
            if cr in cycle:
                return False
            if cr in visit:
                return True
            cycle.add(cr)
            for pr in mydir[cr]:
                if not dfs(pr):
                    return False
            cycle.remove(cr)
            visit.add(cr)
            top.append(cr)
            return True

        for cr in range(numCourses):
            if not dfs(cr):
                return []
        return top