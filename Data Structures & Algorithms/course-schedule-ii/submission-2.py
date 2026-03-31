class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        res = []
        visiting = set()

        def dfs(c):
            if c in visiting:
                return False  # cycle

            if preMap[c] is None:
                return True  # already processed

            visiting.add(c)

            for pre in preMap[c]:
                if not dfs(pre):
                    return False

            visiting.remove(c)

            # mark as processed
            preMap[c] = None

            # add ONCE
            res.append(c)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res