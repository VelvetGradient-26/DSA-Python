from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        small_nums = []

        n = len(nums)

        for i in range(n):
            freq = 0 
            for j in range(n): 
                if j != i and nums[j] < nums[i]: 
                    freq += 1
            small_nums.append(freq)

        return small_nums