class Solution:
    """
      s            e  
    1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0
    k = 2
    num_err = 6 - 3 = 3 > k
    num_err = num_questions - num_correct
    num_err = window_size - num_ones
    num_ones += 1
    if num_err > k: 
        count -= 1
        window_start += 1
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start = 0
        size = 0 
        num_ones = 0 
        
        for window_end in range(len(nums)):
            right_char = nums[window_end]
            if right_char == 1: 
                num_ones +=  1
            num_err = window_end - window_start + 1 - num_ones
            if num_err > k: 
                if nums[window_start] == 1: 
                    num_ones -= 1
                window_start += 1
            
            size = max(window_end-window_start + 1, size)
        
        return size 
            
            
            
        