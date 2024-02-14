def remove(nums, n):
    for num in nums:
        if num == n:
            nums.remove(num)
    return  f'{nums}, k={len(nums)}'

test3= [1,3,4,5,6,2,1,3]
print(remove([1,3,4,5,6,2,1,3], 3)) 