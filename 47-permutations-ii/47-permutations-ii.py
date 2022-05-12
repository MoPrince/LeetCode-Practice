class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        if len(nums)==1:
            return [nums]
        ans = []
        seen = {}
        for i, num in enumerate(nums):
            
            if num not in seen:
                
                seen[num] = 1
                ans += [[num] + arr for arr in self.permuteUnique(nums[:i]+nums[i+1:])]

        return ans