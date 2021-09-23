class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # squares = [0 for x in range(n)] instead of list comprehension we can do one liner to initialize answers array
        squares = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        # where we are going to insert in our square answers array, decrement each time
        highestSquareIdx = right
        while left <= right:
            leftSquare = arr[left] * arr[left]
            rightSquare = arr[right] * arr[right]
            if leftSquare > rightSquare:
                squares[highestSquareIdx] = leftSquare
                left += 1
            else:
                squares[highestSquareIdx] = rightSquare
                right -= 1
            highestSquareIdx -= 1

        return squares
