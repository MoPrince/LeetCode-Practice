class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        flag = 0
        second = []
        
        if len(digits)==0: return [] 

        
        for s in digits:
            
            
            if int(s) == 7:
                
                start_, end = 112,116
            
            elif int(s) == 8:
                
                start_, end = 116,119
            
            elif int(s)==9:
                
                start_, end = 119,123
                                
            else: 
                
                start_, end = 94+3*(int(s)-1), 94+3*(int(s)-1)+3
                
            if flag ==1:
                
                first = [x+y for x in first for y in [chr(i) for i in range(start_,end)]]
                
            else: 
                
                first = [chr(i) for i in range(start_, end)]
                
 
            flag = 1

        return first 