# Pattern Problems
rows = 7
columns = 7

print("# --- Left Triangle --- #")
for row_index in range(rows):
    for column_index in range(columns):
        if column_index <= row_index:
            print("*", end="")
        else:
            print(" ", end="")
    # Moving the cursor to next row
    print()

print()
print("# --- Right Triangle --- #")
for row_index in range(rows):
    for column_index in range(columns):
        if column_index < (rows - 1) - row_index:
            print(" ", end="")
        else:
            print("*", end="")
    # Moving the cursor to next row
    print()

print()
print("# --- Triangle --- #")
for row_index in range(rows // 2, rows):
    for column_index in range(columns):
        if (rows - 1) - row_index <= column_index <= row_index:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
print("# --- Hourglass --- #")
for row_index in range(rows):
    for column_index in range(columns):
        if row_index <= column_index < rows - row_index or (rows - 1) - row_index <= column_index <= row_index:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
print("# --- Side-way Triangle --- #")
for row_index in range(rows):
    for column_index in range(columns):
        if column_index <= row_index and column_index < rows - row_index:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()
print("# --- Zoho Interview Patter --- #")
columns = 11
rows = 11
for row_index in range(rows // 2 + 1):
    for column_index in range(columns):
        if row_index <= column_index < rows - row_index:
            print(abs(rows // 2 - column_index), end='')
        else:
            print(" ", end='')
    print()
