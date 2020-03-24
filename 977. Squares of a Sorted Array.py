def sortedSquares(A):
    result = [x ** 2 for x in A]
    return sorted(result)


print(sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100])
print(sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121])

# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
