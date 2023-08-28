"""
Problem:
https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def __init__(self):
        self.mem = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]

        output = 0

        for i in (1, 2):
            if n - i > 0:
                self.mem[n - i] = self.climbStairs(n - i)
                output += self.mem[n - i]

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(2))
