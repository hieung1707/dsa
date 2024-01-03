"""
Problem:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        needle_idx = 0
        idx = 0
        lock = False
        recall_idx = 1

        while idx < len(haystack):
            ch = haystack[idx]
            if ch == needle[0] and idx != idx - needle_idx and not lock:
                lock = True
                recall_idx = idx

            if ch == needle[needle_idx]:
                needle_idx += 1
                idx += 1

                if needle_idx == len(needle):
                    return idx - len(needle)
            else:
                if lock:
                    idx = recall_idx
                    lock = False
                else:
                    idx += 1
                needle_idx = 0

        return -1


if __name__ == "__main__":
    solution = Solution()
    haystack = "mississippi"
    needle = "issip"
    print(solution.strStr(haystack, needle))
    print(solution.strStr2(haystack, needle))
