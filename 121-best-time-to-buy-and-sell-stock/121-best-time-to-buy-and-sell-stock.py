class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_pro,max_pro = prices[0],  0
        
        for i in prices:
            min_pro = min(i,min_pro);
            
            max_pro = max((i-min_pro),max_pro)
            
        return max_pro
                
        