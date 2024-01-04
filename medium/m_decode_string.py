"""
Problem:
https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def is_number(self, ch: str):
        return '0' <= ch <= '9'

    def decodeString(self, s: str) -> str:
        bracket_index_stack = []
        buffer = []
        output = ""
        current_n_occurrences = ""

        for idx, ch in enumerate(s):
            if ch == "[":
                n_occurrences = int(current_n_occurrences)
                bracket_index_stack.append(n_occurrences)
                buffer.append("")
                current_n_occurrences = ""
            elif ch == "]" and bracket_index_stack:
                n_occurrences = bracket_index_stack.pop()
                buffer_str = buffer.pop() * n_occurrences

                if buffer:
                    buffer[-1] += buffer_str
                else:
                    output += buffer_str
            elif self.is_number(ch):
                current_n_occurrences += ch
            elif buffer:
                buffer[-1] += ch
            else:
                output += ch

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.decodeString(s="3[a]2[bc]"))
    print(solution.decodeString(s="3[a2[c]]"))
    print(solution.decodeString(s="2[abc]3[cd]ef"))
    print(solution.decodeString(s="10[leetcode]"))
