class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        orgn = n
        n = abs(n)
        
        res = 1
        while n:
            res *= x
            n -= 1
        return res if orgn >= 0 else 1 / res