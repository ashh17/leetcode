from collections import Counter


def majorityElement(nums) -> int:
    return max(Counter(nums))


print(majorityElement([3, 4, 3]) == 3)
print(majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2)
# print(majorityElement([3, 3, 4] == 3))

# def majorityElement(nums) -> int:
#     d = {}
#     for x in nums:
#         if x in d:
#             d[x] += 1
#         else:
#             d[x] = 1
#     return max(d.keys())


# Example 1:
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
