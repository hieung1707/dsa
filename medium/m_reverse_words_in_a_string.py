"""
Problem:
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        index = start_w = 0

        while index < len(s):
            if s[index] == " ":
                w = s[start_w:index]
                if w and w != " ":
                    words.insert(0, w)

                start_w = index + 1

            index += 1

        if index - start_w > 0:
            words.insert(0, s[start_w:])

        return " ".join(words)

    """
    This version of reverse words keeps ALL spaces between the words, 
    trimming spaces only at the start and end of the sentence 
    """
    def reverseWordsExreme(self, s: str) -> str:
        output = ""
        index = start_w = 0
        last_eow = None

        while index < len(s):
            if s[index] == " ":
                w = s[start_w:index]
                if w and w != " ":
                    if last_eow is not None:
                        spaces = " " * (start_w - 1 - last_eow)
                        output = spaces + output

                    output = w + output

                    last_eow = index - 1
                start_w = index + 1

            index += 1

        if index - start_w > 0:
            if last_eow:
                spaces = " " * (start_w - 1 - last_eow)
                output = spaces + output
            output = s[start_w:] + output

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))
    print(solution.reverseWords("a good   example"))
    print(solution.reverseWords("  hello world  "))
