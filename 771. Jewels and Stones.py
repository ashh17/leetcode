def numJewelsInStones(J, S):
    result = []
    J = list(J)
    for x in J:
        result.append(S.count(x))
    return sum(result)


# J = "aA"
# S = "aAAbbbb"
# J = "z"
# S = "ZZ"
# print(numJewelsInStones(J,S))
# j = list(J)
# for i in j:
#     print(S.count(i))
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
