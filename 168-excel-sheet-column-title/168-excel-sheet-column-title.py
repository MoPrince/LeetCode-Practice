class Solution:
    def convertToTitle(self, n: int) -> str:
        
        s=''
        
        while n >0:
            
            n -= 1
            s+=chr(65+ n%26)
            n //= 26
            
        
        return s[::-1]