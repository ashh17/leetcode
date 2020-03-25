# def findNumbers(nums) -> int:
#     return sum(len(str(num)) % 2 == 0 for num in nums)

def findNumbers(self, nums: List[int]) -> int:
    def countIt(num):
        count = 0
        while num:
            count += 1
            num //= 10
        return count

    count = 0
    for i in nums:
        if countIt(i) % 2 == 0:
            count += 1
    return count

print(findNumbers([12, 345, 2, 6, 7896]) == 2)

# Example 1:
#
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
