def numberOfSteps(num):
    count = 0
    while num:
        if num % 2 != 0:
            num -= 1
            count += 1
        num //= 2
        if num == 0:
            continue
        count += 1
    return count


nums = [14, 8, 123]
for i in nums:
    print(numberOfSteps(i))

# Input: num = 14
# Output: 6
# Input: num = 8
# Output: 4
# Input: num = 123
# Output: 12
