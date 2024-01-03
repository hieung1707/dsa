"""
Problem:
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        vowel_locs = []
        current_vowels = 0

        for idx, ch in enumerate(s):
            vowel_locs.append(int(ch in vowels))
            if idx < k:
                current_vowels += vowel_locs[idx]

        max_vowels = current_vowels

        for idx in range(len(s) - k):
            current_vowels = current_vowels - vowel_locs[idx] + vowel_locs[idx + k]
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxVowels(s="abciiidef", k=3))
    print(solution.maxVowels(s="aeiou", k=2))
    print(solution.maxVowels(s="leetcode", k=3))
