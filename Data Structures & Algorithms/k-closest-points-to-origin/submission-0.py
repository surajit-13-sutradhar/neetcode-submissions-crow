class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map = {}

        for point in points:
            dist = (point[0])**2 + (point[1])**2
            map[tuple(point)] = dist

        sorted_map = sorted(map.items(), key=lambda x: x[1])

        res = []
        for i in range(k):
            res.append(list(sorted_map[i][0]))
        return res

       