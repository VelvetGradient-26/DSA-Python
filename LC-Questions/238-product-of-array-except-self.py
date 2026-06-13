from typing import List

class Solution:
    """Solution for LeetCode 238: Product of Array Except Self."""

    def brute_product_except_self(self, nums: List[int]) -> List[int]:
        """Brute-force product of array except self (O(n^2))."""
        n = len(nums)
        products = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            products.append(product)

        return products

    def product_except_self(self, nums: List[int]) -> List[int]:
        """Compute product of array except self with O(n) time complexity."""
        result = [1] * len(nums)

        prefix = 1
        for i, num in enumerate(nums):
            result[i] = prefix
            prefix *= num

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result