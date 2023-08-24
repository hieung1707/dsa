"""
Problem:
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        output_str = str(x)

        start = 0
        end = len(output_str) - 1
        while start < end:
            if output_str[start] != output_str[end]:
                return False

            start += 1
            end -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(-121))

    print(solution.isPalindrome(12121))
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(10))
