import random

numbers = [random.randint(1,99) for _ in range(10)]
print(numbers)

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1): 
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums

print(bubble_sort(numbers)) 
