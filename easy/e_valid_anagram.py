"""
Problem:
https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    """
    First we scan through first string to get character count and store it to a character count dict.
    Then we scan second string, gradually reducing the occurrence of each character in character count dict.
        - If the character does not exist in the dict, or the character count after deduction is smaller than 0
        => is not anagram
    """
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}

        if len(s) != len(t):
            return False

        for s_ch in s:
            if s_ch not in char_count:
                char_count[s_ch] = 0

            char_count[s_ch] += 1

        for t_ch in t:
            if t_ch not in char_count or char_count[t_ch] == 0:
                return False

            char_count[t_ch] -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))
