"""
Problem:
https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_index = 0

        for t_index, t_ch in enumerate(t):
            if t_ch == s[s_index]:
                s_index += 1

                if s_index >= len(s):
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence(s="abc", t="ahbgdc"))
    print(solution.isSubsequence(s="axc", t="ahbgdc"))
