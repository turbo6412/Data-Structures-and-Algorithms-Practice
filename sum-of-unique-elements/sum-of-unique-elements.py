class Solution:
    # nums = [1,2,3,2]
    # 1 + 3 = 4 
    # nums = [1,2,3,2]
    # num_freq = {1: 1, 2: 2, 3:1 }
    # sum += if freq < 2
    
    def sumOfUnique(self, nums: List[int]) -> int:
        num_freq = {}
        sum = 0
        
        for i in range(len(nums)): 
            num = nums[i]
            
            if num not in num_freq: 
                num_freq[num] = 0 
            num_freq[num] += 1 
        
        for i in range(len(nums)): 
            num = nums[i]
            if num_freq[num] < 2: 
                sum += num
            else: 
                continue 
        
        return sum 
            