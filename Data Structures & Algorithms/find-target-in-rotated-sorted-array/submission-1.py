class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:  # left sorted
                if nums[l] <= target < nums[m]: # target is on left
                    r = m - 1
                else:
                    l = m + 1
            # right sorted
            else: 
                if nums[m] < target <= nums[r]:  # target is on right
                    l = m + 1
                else:
                    r = m - 1
        return -1