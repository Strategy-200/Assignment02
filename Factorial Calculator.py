# Factorial Calculator
# This program calculates factorial using a loop and shows steps

number = int(input("Enter a number: "))

# Handling negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")

# Handling 0 factorial
elif number == 0:
    print("0! = 1")

else:
    factorial = 1
    steps = ""

    # Loop to calculate factorial
    for i in range(number, 0, -1):
        factorial *= i
        steps += str(i)
        
        if i != 1:
            steps += " × "

    # Display result
    print(f"{number}! = {steps} = {factorial}")