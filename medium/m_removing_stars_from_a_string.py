"""
Problem:
https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def removeStars(self, s: str) -> str:
        char_q = []

        for ch in s:
            if ch == "*":
                if char_q and char_q[-1] != "*":
                    char_q.pop()
            else:
                char_q.append(ch)

        return "".join(char_q)


if __name__ == "__main__":
    solution = Solution()
    print(solution.removeStars(s="leet**cod*e"))
    print(solution.removeStars(s="erase*****"))
    print(solution.removeStars(s="aerase*****"))
