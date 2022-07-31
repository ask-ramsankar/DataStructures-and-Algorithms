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
"""
# Output
# --- Left Triangle --- #
*      
**     
***    
****   
*****  
****** 
*******
"""

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
"""
# Output
# --- Right Triangle --- #
      *
     **
    ***
   ****
  *****
 ******
*******
"""

print()
print("# --- Triangle --- #")
for row_index in range(rows // 2, rows):
    for column_index in range(columns):
        if (rows - 1) - row_index <= column_index <= row_index:
            print("*", end="")
        else:
            print(" ", end="")
    print()
"""
# Output
# --- Triangle --- #
   *   
  ***  
 ***** 
*******
"""

print()
print("# --- Hourglass --- #")
for row_index in range(rows):
    for column_index in range(columns):
        if row_index <= column_index < rows - row_index or (rows - 1) - row_index <= column_index <= row_index:
            print("*", end="")
        else:
            print(" ", end="")
    print()
"""
# Output
# --- Hourglass --- #
*******
 ***** 
  ***  
   *   
  ***  
 ***** 
*******
"""

print()
print("# --- Side-way Triangle --- #")
for row_index in range(rows):
    for column_index in range(columns):
        if column_index <= row_index and column_index < rows - row_index:
            print("*", end="")
        else:
            print(" ", end="")
    print()
"""
# Output
# --- Side-way Triangle --- #
*      
**     
***    
****   
***    
**     
*
"""

print()
print("# --- Zoho Interview Pattern --- #")
columns = 11
rows = 11
for row_index in range(rows // 2 + 1):
    for column_index in range(columns):
        if row_index <= column_index < rows - row_index:
            print(abs(rows // 2 - column_index), end='')
        else:
            print(" ", end='')
    print()
"""
# Output
# --- Zoho Interview Patter --- #
54321012345
 432101234 
  3210123  
   21012   
    101    
     0
"""

print()
print("# --- Zoho Interview Pattern --- #")
columns = 6
rows = 6
for row_index in range(rows):
    for column_index in range(columns):
        if row_index == column_index or row_index == rows - column_index - 1:
            print(rows - column_index if row_index <= rows // 2 else column_index + 1, end='')
        else:
            print(" ", end='')
    print()
"""
# Output
# --- Zoho Interview Patter --- #
5   1
 4 2
  3
 2 4
1   5
"""