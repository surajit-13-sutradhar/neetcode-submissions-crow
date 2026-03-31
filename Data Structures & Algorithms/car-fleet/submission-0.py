class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = [(p, s) for p, s in zip(position, speed)]
        paired.sort(reverse = True)
        
        stack = []
        for p, s in paired:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if the top element (just incoming) is less than or equal to stack[-2] (the previous top element)
                stack.pop()
            
        return len(stack)