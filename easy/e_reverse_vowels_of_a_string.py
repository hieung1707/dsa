"""
Problem:
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        l_ptr = 0
        r_ptr = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)

        while l_ptr < r_ptr:
            l_is_vowel = s[l_ptr].lower() in vowels
            r_is_vowel = s[r_ptr].lower() in vowels

            if l_is_vowel and r_is_vowel:
                s[l_ptr], s[r_ptr] = s[r_ptr], s[l_ptr]
                l_ptr += 1
                r_ptr -= 1

            if not l_is_vowel:
                l_ptr += 1

            if not r_is_vowel:
                r_ptr -= 1

        return "".join(s)


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseVowels("hello"))
    print(solution.reverseVowels("leotcede"))
    print(solution.reverseVowels("aA"))
