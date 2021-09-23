class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        results = []

        for a in range(len(arr)):
            if a > 0 and arr[a - 1] == arr[a]:
                continue
            left = a + 1
            right = len(arr) - 1
            while left < right:
                threeSum = arr[a] + arr[left] + arr[right]

                if threeSum < 0:
                    left += 1

                elif threeSum > 0:
                    right -= 1

                else:
                    results.append([arr[a], arr[left], arr[right]])
                    left += 1
                    while arr[left] == arr[left-1] and left < right:
                        left += 1

        return results
