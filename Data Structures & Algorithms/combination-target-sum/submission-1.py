class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, currtotal):
            if currtotal == target:
                res.append(curr.copy())
                return

            if currtotal > target or i >= len(nums):
                return

            # include nums[i]
            curr.append(nums[i])
            # not incrementing i allows reuse
            dfs(i, curr, currtotal + nums[i])
            curr.pop()

            # exclude nums[i]
            dfs(i + 1, curr, currtotal)

        dfs(0, [], 0)
        return res
        