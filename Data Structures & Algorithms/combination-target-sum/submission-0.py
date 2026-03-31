class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursion
        # two choices
        # include the current num
        # skip the current number

        # optimal backtracking
        # sorting + early stopping
        
        res = []
        nums.sort()

        def dfs(i, currentList, total):
            if total == target:
                res.append(currentList.copy())  # add a copy of currentList to result
                return 
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return # stop the loop
                
                currentList.append(nums[j]) # add nums[j] to currentList
                dfs(j, currentList, total + nums[j])
                currentList.pop()

        dfs(0, [], 0)
        return res