import random

def quick_sort(arr): 
    if len(arr) <= 1: 
        return arr
    
    p = arr[-1]
    L = [x for x in arr[:-1] if  x <= p]
    R = [x for x in arr[:-1] if  x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + [p] + R

numbers = [random.randint(0, 99) for _ in range(10)]
print(numbers)

print(quick_sort(numbers))