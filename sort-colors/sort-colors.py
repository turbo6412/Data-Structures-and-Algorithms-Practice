class Solution:
    def sortColors(self, arr: List[int]) -> None:
        left, mid = 0, 0 
        right = len(arr) - 1

        while mid <= right: 
            if arr[mid] == 2: 
                arr[mid], arr[right] = arr[right], arr[mid]
                right -= 1

            elif arr[mid] == 0: 
                arr[mid], arr[left] = arr[left], arr[mid]
                left += 1 
                mid += 1

            else: 
                mid += 1        
        """
        Do not return anything, modify nums in-place instead.
        """
        
        