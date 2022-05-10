class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = sorted(nums1 + nums2)
        
        t = int(len(nums)/2)
        
        return (nums[t]+nums[t-1])/2 if len(nums)%2==0 else nums[t]
        