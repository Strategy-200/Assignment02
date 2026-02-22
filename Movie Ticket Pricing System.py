# Movie Ticket Pricing System
# Calculates ticket price based on age and day discount

# Taking inputs
age = int(input("Enter age: "))
day = input("Enter day of week: ").strip().lower()
num_tickets = int(input("Enter number of tickets: "))

# Determining base price based on age
if age < 3:
    base_price = 0
    category = "Free"
elif age <= 12:
    base_price = 150
    category = "Child"
elif age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Checking discount based on day
if day in ["friday", "saturday", "sunday"]:
    discount_percent = 20
else:
    discount_percent = 0

# Calculations
total_base = base_price * num_tickets
discount_amount = (total_base * discount_percent) / 100
final_price = total_base - discount_amount

# Display output
print("\n=== TICKET BILL ===")
print("Category:", category)
print(f"Base Price per Ticket: ₹{base_price:.2f}")
print(f"Number of Tickets: {num_tickets}")
print(f"Total Base Price: ₹{total_base:.2f}")
print(f"Discount ({discount_percent}%): ₹{discount_amount:.2f}")
print(f"Price After Discount: ₹{final_price:.2f}")