def majorityElement(nums) -> int:
    count, item = 0, None
    for num in nums:
        if count == 0:
            item = num
        if item == num:
            count += 1
        else:
            count -= 1
    return item


print(majorityElement([3, 4, 3]) == 3)
print(majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2)
print(majorityElement([3, 3, 4]) == 3)

# Example 1:
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
