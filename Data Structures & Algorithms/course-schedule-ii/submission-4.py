class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans=[]
        visitset=set()
        completedset=set()
        premap={i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            premap[course].append(pre)

        def dfs(course):
            if course in visitset:
                return False
            if course in completedset:
                return True
            if len(premap[course])==0:
                completedset.add(course)
                # if course not in completedset:
                ans.append(course)
                return True
            visitset.add(course)
            for pre in premap[course]:
                if not dfs(pre):
                    return False
                
            visitset.remove(course)
            premap[course]=[]
            completedset.add(course)
            ans.append(course)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans
