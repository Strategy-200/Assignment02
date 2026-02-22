# Temperature Converter Program
# Menu-based system for converting temperature between units

while True:
    print("\n=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Exit condition
    if choice == 7:
        print("Exiting program...")
        break

    temperature = float(input("Enter temperature value: "))

    # Conversion logic
    if choice == 1:
        result = (temperature * 9/5) + 32
        print("Result:", f"{result:.2f} F")

    elif choice == 2:
        result = (temperature - 32) * 5/9
        print("Result:", f"{result:.2f} C")

    elif choice == 3:
        result = temperature + 273.15
        print("Result:", f"{result:.2f} K")

    elif choice == 4:
        result = temperature - 273.15
        print("Result:", f"{result:.2f} C")

    elif choice == 5:
        result = (temperature - 32) * 5/9 + 273.15
        print("Result:", f"{result:.2f} K")

    elif choice == 6:
        result = (temperature - 273.15) * 9/5 + 32
        print("Result:", f"{result:.2f} F")

    else:
        print("Invalid choice! Please select from menu.")