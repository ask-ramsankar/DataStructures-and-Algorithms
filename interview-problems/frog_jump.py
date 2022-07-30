"""
@problem Riddle
@statement There are n no of leafs in the pool.
Consider a frog sitting on one of the leaf.
The frog jumping from leaf to leaf as 1 leaf first at first jump,
2 leaves at second, 3 leaves at third jump, and so on.
If the frog continue to jump like this in a loop will it be able to visit all the leaves or not?
"""
import math

# Solution 1
# ------------------------------------- #
n = 16

landed_sum = set()
passed = 0
for i in range(0, n):
    passed += i
    landed_sum.add(passed % n)

if len(landed_sum) == n:
    print("Visit All the Places")
else:
    print("Not Visited All the Places")
# ------------------------------------- #

# Solution 2
# ------------------------------------- #
if math.log2(n) % 1 == 0:
    print("Visit All the Places")
else:
    print("Not Visited All the Places")
# ------------------------------------- #
