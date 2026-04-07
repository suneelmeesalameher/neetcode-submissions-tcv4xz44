class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList={i:[] for i in range(numCourses)}
        visitset=set()
        for course, pre in prerequisites:
                adjacencyList[course].append(pre)
        
        def dfs(course):
            if course in visitset:
                return False
            if len(adjacencyList[course])==0:
                return True
            visitset.add(course)
            for pre in adjacencyList[course]:
                if not dfs(pre):
                    return False
            visitset.remove(course)
            adjacencyList[course]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs): 
                return False
        return True