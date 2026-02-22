# Simple Calculator Program
# This program performs basic arithmetic operations on two numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print("\nResults:")

# Addition
print(f"{n1} + {n2} = {n1 + n2}")

# Subtraction
print(f"{n1} - {n2} = {n1 - n2}")

# Multiplication
print(f"{n1} * {n2} = {n1 * n2}")

# Division (handling division by zero)
print(f"{n1} / {n2} = {n1 / n2:.2f}")

# Modulus
print(f"{n1} % {n2} = {n1 % n2}")

# Exponentiation
print(f"{n1} ^ {n2} = {n1 ** n2}")

