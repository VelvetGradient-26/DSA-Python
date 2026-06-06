from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = 0
        for digit in num: 
            number = number * 10 + digit
        
        number += k

        digit_arr = []
        while(number > 0): 
            dig = number % 10
            digit_arr.append(dig)
            number //= 10

        digit_arr.reverse()
        
        return digit_arr