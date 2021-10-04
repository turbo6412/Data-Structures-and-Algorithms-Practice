import math 
class Solution:
    def threeSumClosest(self, arr: List[int], target_sum: int) -> int:
        arr.sort()
        diff = math.inf
        sum = 0

        for a in range(len(arr)):
            if a > 0 and arr[a-1] == arr[a]:
                continue
            left = a + 1
            right = len(arr) - 1

            while left < right:
                current_sum = arr[a] + arr[left] + arr[right]
                current_diff = abs(current_sum - target_sum)
                if current_diff < diff:
                    sum = current_sum
                    diff = current_diff

                if current_sum < target_sum:
                    left += 1

                elif current_sum > target_sum:
                    right -= 1

                else:
                    return sum
        return sum


