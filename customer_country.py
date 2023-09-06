import csv

customers = open('customers.csv', 'r')

customercountry = open('customer_country.csv', 'w')

csv_file = csv.reader(customers)

next(csv_file)
number = 0
customercountry.write('Full Name , Country\n')
for record in csv_file:
    customercountry.write(f'{record[1]} {record[2]} , {record[4]} \n')
    number += 1

customercountry.write(f'Customers Counted: {number}')
