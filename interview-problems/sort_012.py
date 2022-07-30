"""
@problem Sort
@input List of integers containing (0, 1, 2)
@output sorted list in ascending order 0 -> 1 -> 2
@example:
    -> Input: [1, 0, 2, 1, 0]
    -> Output: [0, 0, 1, 1, 2]
"""
values = [2]

zero_block, current = 0, 1
two_block = len(values) - 1

while current <= two_block:

    if values[zero_block] == 0:
        zero_block += 1
        current = zero_block + 1
        continue

    if values[two_block] == 2:
        two_block -= 1
        continue

    if values[current] == 2:
        values[current], values[two_block] = values[two_block], values[current]
        two_block -= 1
    elif values[current] == 0:
        values[current], values[zero_block] = values[zero_block], values[current]
        zero_block += 1
    else:
        current += 1
    print(values)

print(values)
