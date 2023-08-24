"""
Problem:
https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        q = []

        for ch in s:
            if ch in (parentheses_mapping.values()):
                q.append(ch)
            else:
                if not q:
                    return False

                p = q.pop()
                if p != parentheses_mapping[ch]:
                    return False

        if q:
            return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("([)]"))
    print(solution.isValid("()[]{)[]"))
