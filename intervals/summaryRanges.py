def findRanges(nums):
    if not nums:
        return []

    ranges = []
    start = end = nums[0]

    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            ranges.append(str(start) if start == end else f"{start}->{end}")
            start = end = num

    ranges.append(str(start) if start == end else f"{start}->{end}")

    return ranges

# Example usage
nums1 = [0, 1, 2, 4, 5, 7]
print(findRanges(nums1))  # Output: ["0->2", "4->5", "7"]

nums2 = [0, 2, 3, 4, 6, 8, 9]
print(findRanges(nums2))  # Output: ["0", "2->4", "6", "8->9"]