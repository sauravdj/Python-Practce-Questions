

def first_divisible(nums, divisor):
    for i, num in enumerate(nums):
        if num % divisor == 0:
            return i
    return None
print(first_divisible([101,4,12,24], 2))