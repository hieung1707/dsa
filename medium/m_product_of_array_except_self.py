"""
Problem:
https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        zero_count = 0

        for num in nums:
            if num:
                product_all *= num
            else:
                zero_count += 1

        output = []
        # there are 2 cases when result if index i is 0:
        # - 2 or more zeros are in `nums`
        # - 1 or more zeros and nums[i] is not 0

        for num in nums:
            if zero_count > 1 or (num and zero_count > 0):
                output.append(0)
            elif num == 0:
                output.append(product_all)
            else:
                output.append(product_all // num)

        return output


if __name__ == "__main__":
    solution = Solution()
    # print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
