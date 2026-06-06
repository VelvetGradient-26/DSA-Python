from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] < 9: 
            digits[len(digits) - 1] += 1
            return digits
        
        num = 0
        for digit in digits: 
            num = num * 10 + digit
        
        num += 1
        digit_arr = []
        while (num > 0): 
            dig = num % 10
            digit_arr.append(dig)
            num //= 10

        digit_arr.reverse()
        return digit_arr
