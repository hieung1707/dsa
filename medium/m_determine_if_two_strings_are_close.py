"""
Problem:
https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    """
    The solution may not care about the characters, but only about the occurrences of characters.
    Because they can be easily swapped with each other, we should only compare if both words
        have the same number of characters (doesn't matter which one, just the number of characters is enough)
    You need to take consideration that 2 words must have the same set of characters as well.
    """
    def pattern(self, word: str):
        occurrences_dict = {}

        for ch in word:
            if ch not in occurrences_dict:
                occurrences_dict[ch] = 0

            occurrences_dict[ch] += 1

        pattern_dict = {}
        for ch, occurrence_count in occurrences_dict.items():
            if occurrence_count not in pattern_dict:
                pattern_dict[occurrence_count] = 0

            pattern_dict[occurrence_count] += 1

        return pattern_dict, set(occurrences_dict.keys())

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        pattern_dict_1, unique_chars_1 = self.pattern(word1)
        pattern_dict_2, unique_chars_2 = self.pattern(word2)

        if (len(pattern_dict_1) != len(pattern_dict_2)) or (unique_chars_1 != unique_chars_2):
            return False

        for occurrence_count in pattern_dict_1:
            n_characters_1 = pattern_dict_1.get(occurrence_count)
            n_characters_2 = pattern_dict_2.get(occurrence_count)

            if not (n_characters_1 and n_characters_2) or (n_characters_1 != n_characters_2):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.closeStrings(word1="abc", word2="bca"))
    print(solution.closeStrings(word1="a", word2="aa"))
    print(solution.closeStrings(word1="cabbba", word2="abbccc"))
    print(solution.closeStrings(word1="uau", word2="ssx"))
