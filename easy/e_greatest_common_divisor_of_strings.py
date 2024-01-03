"""
Problem:
https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def gcd(self, x, y):
        if y == 0:
            return x

        return self.gcd(y, x % y)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        gcd_len = self.gcd(len(str1), len(str2))
        divisor = str1[:gcd_len]
        if (len(str1) // gcd_len) * divisor == str1 and (len(str2) // gcd_len) * divisor == str2:
            return str1[:gcd_len]

        return ""


if __name__ == "__main__":
    solution = Solution()
    str1 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
    str2 = "NLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGMNLZGM"
    print(solution.gcdOfStrings(str1, str2))
