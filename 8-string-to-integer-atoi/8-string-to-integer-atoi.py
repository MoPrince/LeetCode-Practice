class Solution:
    def myAtoi(self, s: str) -> int:
        
        n, t, flag = 0, 1, True
    
        
        for i in s:
            
            
            if i == ' ' and flag:
                
                continue
                
            
            
            elif i == '+' and flag:
                
                flag = False
                
                continue
                
                
            elif i== '-' and flag:
                
                flag = False
                
                t = -1
                
                continue
                
                    
                
            try: 
                
                flag = False
                
                n = n*10 + int(i)


            except:

                    return min(max(n*t, -2147483648),2147483647)
                        
                        
                        
        return min(max(n*t, -2147483648),2147483647)

                    
            
            