def countSmaller(nums):
    result = [0] * len(nums)
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            if nums[j] < nums[i]:
                result[i] += 1
    return result


nums = [5, 2, 6, 1]
print(countSmaller(nums))
# its in the order of n^2, need to improve it
