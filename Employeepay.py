import csv

employee = open('EmployeePay.csv', 'r')

csv_file = csv.reader(employee)

next(csv_file)
for record in csv_file:
    salary = int(record[3])
    bonus = int(record[3]) * float(record[4])
    pay = int(record[3]) + bonus
    print(f'First Name: {record[1]}')
    print(f'Last Name: {record[2]}')
    print(f'Salary: $   {salary:10,.2f}')
    print(f'Bonus:  $   {bonus:10,.2f}')
    print(f'Pay:    $   {pay:10,.2f}')
    input()
