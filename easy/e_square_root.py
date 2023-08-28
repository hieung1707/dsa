"""
Problem:
https://leetcode.com/problems/sqrtx/
"""


class Solution:
    def _search(self, start: int, end: int, target: int):
        if start >= end:
            return start
        elif start + 1 == end:
            if end * end <= target:
                return end

            return start

        mid = (start + end) // 2

        if target <= mid * mid:
            return self._search(start, mid, target)

        return self._search(mid, end, target)

    def mySqrt(self, x: int) -> int:
        if x in (0, 1):
            return x

        return self._search(1, x // 2, x)


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(24))
