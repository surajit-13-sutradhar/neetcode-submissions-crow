class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # have to decide whether to take an element or reject it
        res = set()
        candidates.sort()

        def backtrack(idx, curr, currtotal):
            if currtotal == target:
                res.add(tuple(curr))
                return
            
            if currtotal >= target or idx == len(candidates):
                return

            curr.append(candidates[idx])
            backtrack(idx + 1, curr, currtotal + candidates[idx])
            curr.pop()

            backtrack(idx + 1, curr, currtotal)

        backtrack(0, [], 0)
        return [list(combination) for combination in res]
