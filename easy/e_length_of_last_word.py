"""
Problem:
https://leetcode.com/problems/length-of-last-word/
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end_idx = None

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " " and end_idx is None:
                end_idx = i
            elif end_idx is not None and s[i] == " ":
                return end_idx - i

        if end_idx is not None:
            return end_idx + 1

        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
    print(solution.lengthOfLastWord("luffy is still joyboy"))
