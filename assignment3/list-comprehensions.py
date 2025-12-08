import csv
with open("../csv/employees.csv") as f:
    reader = csv.reader(f)
    employees = list(reader)   
names = [row[1] + " " + row[2] for row in employees[1:]]
print("All employee names:")
print(names)
names_with_e = [name for name in names if "e" in name.lower()]
print("\nEmployee names containing the letter 'e':")
print(names_with_e)
