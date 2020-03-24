def subtractProductAndSum(n: int) -> int:
    result = []
    prod = 1
    while (n):
        digit = n % 10
        result.append(digit)
        n //= 10
        prod *= digit
    return prod - sum(result)


print(subtractProductAndSum(234))

# Example 1:
#
# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15
#
# Example 2:
#
# Input: n = 4421
# Output: 21
# Explanation:
# Product of digits = 4 * 4 * 2 * 1 = 32
# Sum of digits = 4 + 4 + 2 + 1 = 11
# Result = 32 - 11 = 21
