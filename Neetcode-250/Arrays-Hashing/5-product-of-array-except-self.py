from typing import List

class Solution:
    def bruteProductExceptSelf(self, nums: List[int]) -> List[int]:
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

    def productExceptSelf(self, nums: List[int]) -> List[int]:
            result = [1] * len(nums)

            prefix = 1
            for i in range(len(nums)): 
                result[i] = prefix
                prefix *= nums[i]

            postfix = 1
            for i in range(len(nums)-1, -1, -1): 
                result[i] *= postfix
                postfix *= nums[i]

            return result