height = int(input("Enter height: "))

# Pattern 1: Increasing numbers
print("Pattern 1: Increasing numbers")
for i in range(1, height + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 2: Repeating row numbers
print("\nPattern 2: Repeating row numbers")
for i in range(1, height + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# Pattern 3: Reverse decreasing pattern
print("\nPattern 3: Reverse decreasing pattern")    
for i in range(height, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Pattern 4: Pyramid pattern
print("\nPattern 4: Pyramid pattern")   
for i in range(1, height + 1):
# Increasing part
    for j in range(1, i + 1):
        print(j, end="")
# Decreasing part
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
