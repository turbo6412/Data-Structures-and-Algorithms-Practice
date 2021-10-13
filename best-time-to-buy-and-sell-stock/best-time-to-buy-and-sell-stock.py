class Solution:
#     prices = [7,1,5,3,6,4]
# min = 7
# profit1 -= arr[i] -min
# profit = max(profit, profit1)
    def maxProfit(self, arr: List[int]) -> int:
        c_min = float('inf') 
        profit = float('-inf') 
        
        for i in range(len(arr)): 
            c_min = min(arr[i], c_min)
            current_profit = arr[i] - c_min 
            profit = max(current_profit, profit)
        
        return profit 