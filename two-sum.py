class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            secound_nums = nums.copy()
            secound_nums.remove(i)
            for j in secound_nums:
                if i + j == target:
                    return [nums.index(i), secound_nums.index(j) + 1]
