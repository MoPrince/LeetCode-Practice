class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        prev = arr[1]-arr[0]
        
        for i in range (1,len(arr)-1):
            
            cur = arr[i+1]-arr[i]
            
            if cur != prev:
                
                return False
            
            
        return True