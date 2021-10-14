class Solution:
    """
        Input: s1 = "abc" s2 = "eidbacooo"
        Output: True
        Explanation: s2 contains one permutation of s1 ("ba")."""

    def checkInclusion(self, pattern: str, str2: str) -> bool:
        window_start = 0
        pattern_count = {}
        perm_count = 0
        size = 0

        # store pattern char in hash table
        for char in pattern:
            if char not in pattern_count:
                pattern_count[char] = 0
            pattern_count[char] += 1

        for window_end in range(len(str2)):
            right_char = str2[window_end]
            if right_char in pattern_count:
                pattern_count[right_char] -= 1
                # increment if contains character in pattern
                if pattern_count[right_char] >= 0:
                    perm_count += 1

            # shrinking when go over pattern
            if window_end - window_start + 1 > len(pattern):
                left_char = str2[window_start]
                if left_char in pattern_count:

                    if pattern_count[left_char] >= 0:
                        perm_count -= 1
                    pattern_count[left_char] += 1
                window_start += 1

            # have valid window lets check if contains everything in pattern
            if perm_count == len(pattern):
                return True

        return perm_count == len(pattern)
