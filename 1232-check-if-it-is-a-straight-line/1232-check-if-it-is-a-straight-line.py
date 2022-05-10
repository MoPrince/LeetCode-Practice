class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        
        return False if any((c[i][0]*(c[i+1][1]-c[i+2][1])+  
               c[i+1][0]*(c[i+2][1]-c[i][1])+
               c[i+2][0]*(c[i][1]-c[i+1][1]))!=0 
               for i in range(len(c)-2)) else True