import math 

class Solution:
                  
    # [1, 12, -5, -6, 50, 3]
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_start = 0 
        max_avg = -math.inf
        current_sum = 0
        for window_end in range(len(nums)): 
            current = nums[window_end]
            current_sum += current
            size = window_end - window_start + 1
            if size >= k: 
                max_avg = max(max_avg, (current_sum/k) )  
                current_sum -= nums[window_start]
                window_start += 1
                
        return max_avg
                
                
            
        