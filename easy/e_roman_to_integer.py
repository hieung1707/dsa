"""
Problem:
https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    ROMAN_TO_INT_DICT = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        output = 0

        for idx in range(len(s)):
            num = self.ROMAN_TO_INT_DICT[s[idx]]

            if idx != len(s) - 1 and self.ROMAN_TO_INT_DICT[s[idx + 1]] > num:
                num = -num

            output += num

        return output


if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))
