from typing import List
class Solution:
    def maxSubArray_bruteforce(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        
        subarrays = []

        for i in range(n): 
            for j in range(i, n): 
                subarr = []
                for k in range(i, j+1): 
                    subarr.append(nums[k])
                subarrays.append(subarr)

        maximum = float("-inf")
        for arr in subarrays: 
            if sum(arr) > maximum: 
                maximum = sum(arr)

        return maximum
