class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(len(nums)): 
            if i > 0 and nums[i-1] > 0: 
                nums[i] += nums[i-1]
        return max(nums)