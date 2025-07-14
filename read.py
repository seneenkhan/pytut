emp_file = open("employee", "r")
for employee in emp_file.readlines():
    print(employee)
emp_text = emp_file.close()
