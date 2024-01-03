"""
Problem:
https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        output = ""

        for i in range(max(word1_len, word2_len)):
            w1_character = ""
            w2_character = ""

            if i < word1_len:
                w1_character = word1[i]

            if i < word2_len:
                w2_character = word2[i]

            output += w1_character + w2_character

        return output


if __name__ == "__main__":
    solution = Solution()
    word1 = "abc"
    word2 = "pqr"
    print(solution.mergeAlternately(word1, word2))
