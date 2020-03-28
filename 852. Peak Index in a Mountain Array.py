# Example 1:
#
# Input: [0,1,0]
# Output: 1
#
# Example 2:
#
# Input: [0,2,1,0]
# Output: 1
#

def peakIndexInMountainArray(A) -> int:
    for i in range(len(A)):
        if A[i] > A[i + 1]:
            return i


print(peakIndexInMountainArray([0, 1, 0]))
print(peakIndexInMountainArray([0, 2, 1, 0]))
print(peakIndexInMountainArray([3, 4, 5, 1]))
