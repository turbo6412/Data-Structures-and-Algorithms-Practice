class Solution:
#  b s
# [7,1,5,3,6,4]

# max(profit) = 5
# update minimum each iteration
# max(profit) = s - b
# return profit after loop ends
    def maxProfit(self, arr: List[int]) -> int:
        profit = 0 
        buy = float('inf') 
        sell = 0 
        
        for i in range(len(arr)):
            current_price = arr[i]
            buy = min(buy, current_price)
            diff = current_price - buy 
            profit = max(profit, diff)
        return profit 
            