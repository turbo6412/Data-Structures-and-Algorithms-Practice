class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        
        results = []
        arr.sort()
        for a in range(len(arr)):
            if a > 0 and arr[a-1] == arr[a]:
                continue

            left = a + 1
            right = len(arr) - 1
            while left < right:
                current_sum = arr[a] + arr[left] + arr[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:  # equal case
                    results.append([arr[a], arr[left], arr[right]])
                    left += 1
                    while arr[left] == arr[left-1] and left < right:
                        left += 1

        return results
