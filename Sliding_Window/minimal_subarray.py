def minSubArrayLen(target, nums):
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0