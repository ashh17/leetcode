# Example 1:
#
# Input: mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3
# Output: [2,0,3]
# Explanation:
# The number of soldiers for each row is:
# row 0 -> 2
# row 1 -> 4
# row 2 -> 1
# row 3 -> 2
# row 4 -> 5
# Rows ordered from the weakest to the strongest are [2,0,3,1,4]
#
# Example 2:
#
# Input: mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2
# Output: [0,2]
# Explanation:
# The number of soldiers for each row is:
# row 0 -> 1
# row 1 -> 4
# row 2 -> 1
# row 3 -> 1
# Rows ordered from the weakest to the strongest are [0,2,3,1]


def kWeakestRows(mat, k):
    result = []
    for enum, x in enumerate(mat):
        result.append((enum, sum(x)))
    result.sort(key=lambda tup: tup[1])
    result = [i[0] for i in result]
    return result[:k]


print(kWeakestRows([[1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1]], 3))

print(kWeakestRows([[1, 0, 0, 0],
                    [1, 1, 1, 1],
                    [1, 0, 0, 0],
                    [1, 0, 0, 0]], 2))

# result = []
# for enum, x in enumerate(mat):
#     result.append((enum, sum(x)))
# result.sort(key=lambda tup: tup[1])
# print([i[0] for i in result])
