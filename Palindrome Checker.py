# Palindrome Checker
# Checks whether a word or number is palindrome

user_input = input("Enter word/number: ")

# Original value
original_value = user_input

# Convert to lowercase for comparison (ignore case)
processed_value = user_input.lower()

# Reverse the string
reversed_value = processed_value[::-1]

# Display steps
print("\nOriginal:", original_value)
print("Reversed:", reversed_value)

# Check palindrome
if processed_value == reversed_value:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")