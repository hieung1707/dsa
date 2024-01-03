"""
Problem:
https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def get_number_string(self, number: int):
        """
        This is hand-crafted version, in case other languages don't support int-string conversion.
        In case of python, using str() would be more convenient (and maybe faster also)
        """
        number_str = ""
        while number:
            number_str = str(number % 10) + number_str
            number //= 10

        return number_str

    def modify_char_array(self, chars, current_compressed_len: int, current_char: str, sequence_len: int):
        if not current_char:
            return current_compressed_len

        chars[current_compressed_len] = current_char
        current_compressed_len += 1

        if sequence_len > 1:
            number_str = self.get_number_string(sequence_len)
            chars[current_compressed_len: current_compressed_len + len(number_str)] = number_str
            current_compressed_len += len(number_str)

        return current_compressed_len

    def compress(self, chars: List[str]) -> int:
        current_char = None
        start_idx = 0
        compressed_len = 0

        for idx, char in enumerate(chars):
            if char != current_char:
                sequence_len = idx - start_idx
                compressed_len = self.modify_char_array(chars, compressed_len, current_char, sequence_len)

                start_idx = idx
                current_char = char

        if current_char:
            remaining_len = len(chars) - start_idx
            compressed_len = self.modify_char_array(chars, compressed_len, current_char, remaining_len)

        print(chars[:compressed_len])

        return compressed_len

    # --------------------------------------------------------------------------
    """
    Editorial solution
    """
    def editorial(self, chars: List[str]):
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))
    print(solution.compress(["a"]))
    print(solution.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
