def smallerNumbersThanCurrent(nums):
    result = [0] * len(nums)
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue
            if nums[j] < nums[i]:
                result[i] += 1
    return result


nums = [8, 1, 2, 2, 3]
nums = [6, 5, 4, 8]
nums = [7, 7, 7, 7]
print(smallerNumbersThanCurrent(nums))
