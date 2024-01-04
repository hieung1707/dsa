"""
Problem:
https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:

    def __init__(self):
        self.history = []

    def ping(self, t: int) -> int:
        self.history.append(t)
        lower_bound = t - 3000

        while self.history:
            if self.history[0] < lower_bound:
                self.history.pop(0)
                continue

            break

        return len(self.history)


if __name__ == "__main__":
    solution = Solution()
    for t in [1, 100, 3001, 3002]:
        print(solution.ping(t))
