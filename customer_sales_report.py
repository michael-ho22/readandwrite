import csv

salesreport = open('sales.csv', 'r')
csv_file = csv.reader(salesreport)
next(csv_file)

sales = open('salesreport.csv', 'w', newline = '')
salestotal = csv.writer(sales)

lst = []

for record in csv_file:
    
    total = float(record[3]) + float(record[4]) + float(record[5])
    customer_id = record [0]
    in_record = False

    for x in lst:
        if x[0] == customer_id:
            x[1] += total
            in_record = True

    if in_record == False:
        lst.append([customer_id, total])

sales.write('Customer ID, Total\n')
        
for customer_id, total in lst:
    salestotal.writerow([customer_id,  round(total, 2)])
