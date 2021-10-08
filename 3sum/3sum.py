class Solution:

# a + l + r = 0 
    # [-1,0,-1,-1,2,-4]
    # sort array 
#        a           lr
    #  [-4, -1, -1, -1, -1, 0, 2]

    # [ [-1,-1,2],[-1,-1,2], [-1,0,1] ]
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        results = []
        
        for a in range(len(arr)): 
            if a > 0 and arr[a] == arr[a-1]: 
                continue 
            left = a + 1 
            right = len(arr) - 1
            
            while left < right: 
                current_sum = arr[a] + arr[left] + arr[right]
                
                if current_sum < 0: 
                    left += 1
                
                elif current_sum > 0: 
                    right -= 1
                
                else: # equal 
                    results.append([ arr[a], arr[left], arr[right] ])
                    left += 1
                    while left < right and arr[left-1] == arr[left]: 
                        left += 1
            
        return results 
                
        