class Solution:
    def findUnsortedSubarray(self, arr):
        if len(arr) < 2:
            return 0

        window_end = 0
        max_val = arr[0]
        for i in range(len(arr)):

            if arr[i] < max_val:
                window_end = i

            max_val = max(arr[i], max_val)

        window_start = len(arr) - 1
        min_val = arr[len(arr) - 1]

        i = len(arr) - 1

        while i >= 0:
            if arr[i] > min_val:
                window_start = i

            min_val = min(arr[i], min_val)
            i -= 1

        size = window_end - window_start + 1
        # if it's sorted already window_end will just stay at index 0 (can draw this out to see)
        if window_end != 0:
            return size
        return 0
    