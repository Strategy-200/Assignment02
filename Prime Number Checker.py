# Prime Number Checker
# Part 1: Check single number
# Part 2: Find primes in a range

# Part 1
number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is NOT a prime number")

else:
    is_prime = True

    # Check divisibility from 2 to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a PRIME number")
    else:
        print(f"{number} is NOT a prime number")


# Part 2
start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for num in range(start, end + 1):
    
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")