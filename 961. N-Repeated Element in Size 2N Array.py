# Example 1:
#
# Input: [1,2,3,3]
# Output: 3
#
# Example 2:
#
# Input: [2,1,2,5,3,2]
# Output: 2
#
# Example 3:
#
# Input: [5,1,5,2,5,3,5,4]
# Output: 5

def repeatedNTimes(self, A: List[int]) -> int:
    for x in A:
        if A.count(x) > 1:
            return x
