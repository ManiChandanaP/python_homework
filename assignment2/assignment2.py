import csv
import traceback
import os
from datetime import datetime
import custom_module

# Task 2
def read_employees():
    employees_dict = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r", newline="") as f:
            reader = csv.reader(f)
            first = True
            for row in reader:
                if first:
                    employees_dict["fields"] = row
                    first = False
                else:
                    rows.append(row)
        employees_dict["rows"] = rows
        return employees_dict
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()
employees = read_employees()
print(employees)


#task3
def column_index(first_name):
    try:
        return employees["fields"].index(first_name)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

employee_id_column = column_index("employee_id")
print("employee_id_column =", employee_id_column)

#task4
def first_name(row_number):
    try:
        first_name_column = column_index("first_name")
        row = employees["rows"][row_number]
        return row[first_name_column]
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()
 
 #task5
def employee_find(employee_id):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id
        matches = list(filter(employee_match, employees["rows"]))
        return matches

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

#task6
def employee_find_2(employee_id):
    try:
        matches = list(
            filter(lambda row: int(row[employee_id_column]) == employee_id,
                   employees["rows"])
        )
        return matches
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

#task7
def sort_by_last_name():
    try:
        last_col = column_index("last_name")
        employees["rows"].sort(key=lambda row: row[last_col])
        return employees["rows"]

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()
print(sort_by_last_name())

#task8
def employee_dict(row):
    try:
        result = {}
        fields = employees["fields"]
        for i in range(len(fields)):
            field = fields[i]
            if field == "employee_id":  # skip employee_id
                continue
            result[field] = row[i]
        return result
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()
print(employee_dict(employees["rows"][0]))


# Task 9
def all_employees_dict():
    try:
        result = {}
        for row in employees["rows"]:
            emp_id = row[employee_id_column]  
            result[emp_id] = employee_dict(row)
        return result
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, '
                f'Func.Name : {trace[2]}, Message : {trace[3]}'
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()
        
#task10
def get_this_value():
    return os.getenv("THISVALUE")

#task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("supersecret!")
print(custom_module.secret)

#task 12
def read_csv_to_min_dict(file_path):
    minutes = {"fields": [], "rows": []}
    try:
        with open(file_path, "r", newline="") as f:
            reader = csv.reader(f)
            first = True
            for row in reader:
                if first:
                    minutes["fields"] = row
                    first = False
                else:
                    minutes["rows"].append(tuple(row))
        return minutes
    except Exception as e:
        # Provide traceback info if something goes wrong
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

def read_minutes():
    minutes1 = read_csv_to_min_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_min_dict("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print("minutes1:", minutes1)
print("minutes2:", minutes2)


#task 13
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)
minutes_set = create_minutes_set()
print(minutes_set)


#task 14
def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return converted
write_sorted_list()