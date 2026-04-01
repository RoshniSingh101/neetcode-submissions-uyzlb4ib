class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course prereq to an empty list
        preMap = {i:[] for i in range(numCourses)}

        # add all prereqs to respective courses
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # add visit set to keep track of courses in DFS path
        visitSet = set()

        def dfs(crs):
            # detected a loop
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = [] # if encounter empty list, course doesn't have prereq and can return true
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


