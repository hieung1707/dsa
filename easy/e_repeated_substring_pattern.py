"""
Problem:
https://leetcode.com/problems/repeated-substring-pattern/
"""
from math import sqrt


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        divisors = set()
        s_len = len(s)

        for i in range(1, s_len // 2 + 1):
            if s_len % i == 0:
                divisors.add(i)

        for divisor in reversed(list(divisors)):
            sub_str = s[:divisor]
            is_repeated = True

            for j in range(divisor, s_len, divisor):
                if s[j:j + divisor] != sub_str:
                    is_repeated = False
                    break

            if is_repeated:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.repeatedSubstringPattern("abcabc"))
