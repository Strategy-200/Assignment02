# Sum and Average Calculator
# This program takes multiple numbers and calculates sum, average, max, and min

count = int(input("How many numbers? "))

total_sum = 0
maximum = None
minimum = None

for i in range(1, count + 1):
    num = int(input(f"Enter number {i}: "))
    
    total_sum += num

    # Initialize max and min
    if maximum is None or num > maximum:
        maximum = num

    if minimum is None or num < minimum:
        minimum = num

# Calculating average
average = total_sum / count

# Display results
print("\nResults:")
print("Sum:", total_sum)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)