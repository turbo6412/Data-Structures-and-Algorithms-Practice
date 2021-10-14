class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for window_end in range(len(nums)): 
            if window_end > 0 and nums[window_end-1] > 0: 
                nums[window_end] += nums[window_end-1]
        return max(nums)