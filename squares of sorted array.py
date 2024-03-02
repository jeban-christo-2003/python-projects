def sortedSquares(self, nums: List[int]) -> List[int]:
    nums = [num ** 2 for num in nums]
    nums.sort()
    return nums
nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]

print(sortedSquares(nums1))
print(sortedSquares(nums2))
