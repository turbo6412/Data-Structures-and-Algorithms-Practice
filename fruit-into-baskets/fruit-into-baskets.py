class Solution:
    def totalFruit(self, str1: List[int]) -> int:
        window_start = 0
        char_count = {}
        size = 0

        for window_end in range(len(str1)):
            char = str1[window_end]
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1

            while len(char_count) > 2:
                start_char = str1[window_start]
                char_count[start_char] -= 1
                if char_count[start_char] == 0:
                    del char_count[start_char]
                window_start += 1

            size = max(size, window_end - window_start + 1)
        return size