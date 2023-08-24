"""
Problem:
https://leetcode.com/problems/3sum/
"""


from typing import List, Set


class Solution:
    def twoSum(self, nums: List[int], start: int, end: int, target_num: int) -> Set[List[int]]:
        mem = {}
        outputs = set()

        for idx in range(start, end + 1):
            num = nums[idx]

            if num in mem:
                outputs.add(sorted((target_num, mem[num], num)))

            mem[-target_num - num] = num

        return outputs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outputs = set()

        nums_len = len(nums)
        for i in range(nums_len):
            res = self.twoSum(nums, start=i + 1, end=nums_len - 1, target_num=nums[i])

            outputs = outputs.union(res)

        return outputs


class OptimizedSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Self-explanation:
        - Sort the array so that the array will have the pattern of increasing indexes -> increasing sum
        - Anker 1 index i, scan the range [i + 1, len]
            +
        """
        target = 0
        nums.sort()
        s = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)

        return output


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    solution = OptimizedSolution()
    print(solution.threeSum(nums))
