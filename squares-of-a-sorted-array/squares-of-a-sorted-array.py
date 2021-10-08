# [-4,-1,0,3,10]
#       l                r
# [-11, -1, 0, 1, 2, 3, 10]

# results = [100, 16, 9]
#                           i
# results = [0, 0, 0, 0, 0, 0, 121]
 # [9, 16, 100]
class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        results = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        index = len(arr) - 1
        
        while left <= right:
            sq_left = arr[left] * arr[left]
            sq_right = arr[right] * arr[right] 
            
            if sq_left > sq_right:
                results[index] = sq_left
                left += 1
            
            # right and equal case 
            else: 
                results[index] = sq_right
                right -= 1
                
            index -= 1
        return results 
        
        

        