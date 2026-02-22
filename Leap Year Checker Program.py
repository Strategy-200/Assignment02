# Leap Year Checker Program
# A year is leap if divisible by 4 AND (not divisible by 100 OR divisible by 400)

# Taking year input
year = int(input("Enter a year: "))

# Checking leap year condition
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    is_leap = True
else:
    is_leap = False

# Displaying result with reason
print("\n=== Leap Year Analysis ===")
print("Year:", year)

if is_leap:
    print("Result: Leap Year")
    
    if year % 400 == 0:
        print("Reason: Divisible by 400")
    elif year % 4 == 0 and year % 100 != 0:
        print("Reason: Divisible by 4 but not by 100")

else:
    print("Result: NOT a Leap Year")
    
    if year % 4 != 0:
        print("Reason: Not divisible by 4")
    elif year % 100 == 0 and year % 400 != 0:
        print("Reason: Divisible by 100 but not by 400")