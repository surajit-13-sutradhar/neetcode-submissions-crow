class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] > 1:
                return num
