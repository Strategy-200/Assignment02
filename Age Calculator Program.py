# Age Calculator Program
# This program calculates age in different units

# Taking birth year input
birth_year = int(input("Enter your birth year (YYYY): "))

# Getting current year
current_year = 2026

# Calculating age in years
age_years = current_year - birth_year

print("\nApproximate Age Calculations:")
print("Current Age:", age_years, "years")
print("Age in Months:", age_years * 12)
print("Age in Days:", age_years * 365)
print("Age in Hours:", age_years * 365 * 24)
print("Age in Minutes:", age_years * 365 * 24 * 60)
print("Years until 100:", 100 - age_years)
