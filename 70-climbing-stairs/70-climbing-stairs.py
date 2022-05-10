class Solution:
    def climbStairs(self, n: int) -> int:
        cur, prev = 1, 0
        
        while n!=0:
            
            prev, cur, n = cur, prev+cur, n-1
            
            
            
        return cur