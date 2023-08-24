"""
Problem:
https://leetcode.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        output = ""
        mod = 0
        len_a = len(a)
        len_b = len(b)
        i = 0

        while i < min(len_a, len_b):
            bit_a = int(a[len_a - 1 - i])
            bit_b = int(b[len_b - 1 - i])

            val = bit_a + bit_b + mod
            mod = val // 2
            val = val % 2
            output = str(val) + output

            i += 1

        if i <= len_a - 1:
            while i < len_a:
                bit_a = int(a[len_a - 1 - i])
                val = bit_a + mod
                mod = val // 2
                val = val % 2
                output = str(val) + output

                i += 1

        if i <= len_b - 1:
            while i < len_b:
                bit_b = int(b[len_b - 1 - i])
                val = bit_b + mod
                mod = val // 2
                val = val % 2
                output = str(val) + output

                i += 1

        if mod:
            output = str(mod) + output

        return output


if __name__ == "__main__":
    solution = Solution()
    a = "11"
    b = "111"
    print(solution.addBinary(a, b))
