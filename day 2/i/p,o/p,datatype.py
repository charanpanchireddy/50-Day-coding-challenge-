# Student Information Program

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks (out of 100): "))
is_hosteller = input("Are you a hosteller? (yes/no): ")

# Processing data
next_year_age = age + 1
passed = marks >= 35
is_hosteller = (is_hosteller.lower() == "yes")

# Displaying output
print("\n--- Student Details ---")
print("Name:", name)
print("Current Age:", age)
print("Age Next Year:", next_year_age)
print("Marks:", marks)
print("Result:", "Pass ✅" if passed else "Fail ❌")
print("Hosteller:", is_hosteller)
