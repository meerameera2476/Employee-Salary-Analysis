# Employee Salary Analysis

employees = {
    "Ravi": 25000,
    "Priya": 30000,
    "Karthik": 28000,
    "Divya": 35000,
    "Arun": 27000
}

# Average Salary
average_salary = sum(employees.values()) / len(employees)

# Highest Salary
highest_paid = max(employees, key=employees.get)

# Lowest Salary
lowest_paid = min(employees, key=employees.get)

print("----- Employee Salary Analysis -----")
print("Average Salary:", average_salary)
print("Highest Paid Employee:", highest_paid, "-", employees[highest_paid])
print("Lowest Paid Employee:", lowest_paid, "-", employees[lowest_paid])

print("\nEmployee Salaries:")
for name, salary in employees.items():
    print(name, ":", salary)