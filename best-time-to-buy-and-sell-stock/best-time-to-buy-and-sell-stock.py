class Solution:
    """
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    
             i 
    [7,1,5,3,6,4]
    5-1, 3-1, 6-1, 4-1
    
    # find smallest entry point to buy stock
    """
    def maxProfit(self, arr: List[int]) -> int:
        profit = 0
        start_price = float('inf')
        
        for i in range(len(arr)):
            start_price = min(start_price, arr[i])
            current_prof = arr[i] - start_price
            profit = max(profit, current_prof)
        
        return profit 