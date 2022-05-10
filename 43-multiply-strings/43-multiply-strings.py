class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        nums, result1, result2 = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}, 0, 0
        
        for i in num1:
            result1 = result1*10+ nums[i]
            
        for i in num2: 
            result2 = result2*10+ nums[i]
            
            
        return(str(result1*result2))