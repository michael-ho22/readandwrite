import csv

salesreport = open('sales.csv', 'r')

csv_file = csv.reader(salesreport)

sales = open('salesreport.csv', 'w', newline = '')


lst = {}

next(csv_file)

for record in csv_file:
    customer_id = record[0]
    total = float(record[3]) + float(record[4]) + float(record[5])

    if customer_id in lst:
        lst[customer_id] += total
    else:
        lst[customer_id] = total

totalsales = csv.writer(sales)

totalsales.writerow(['Customer ID', ' Total'])

for customer_id, total in lst.items():
    totalsales.writerow([customer_id,  round(total,2)])

# atotal = 0
# btotal = 0
# ctotal = 0
# dtotal = 0
# etotal = 0
# ftotal = 0
# gtotal = 0
# htotal = 0
# itotal = 0
# jtotal = 0
# ktotal = 0
# ltotal = 0

# sales.write('Customer ID,  Total\n')
# next(csv_file)
# # lst = list(csv_file)
# # startID = lst[0]
# custID = set()
# for record in csv_file:
#     idnum = record[0]
#     total = float(record[3]) + float(record[4]) + float(record[5])
        
#     if idnum in custID:
#         custID[idnum] += total
    
#     elif idnum not in custID:
#         custID.append
#         custID[idnum] = total

# for idnum in custID.items():
#     sales.write(f'{idnum},   ${total}\n')

# for record in csv_file:
#     idnum = record[0]
#     total = float(record[3]) + float(record[4]) + float(record[5])
#     if idnum not in custID:
#         custID.append(idnum)
#         custID[idnum] = total
#         sales.write(f'{idnum},  ')
#         # sales.write(f'{idnum},    ${total:10,.2f}\n')
#     elif idnum in custID:
#         total = total + nexttotal
#         sales.write(f' ${newtotal:10,.2f}\n')

#############################################################

# for record in csv_file:
#     idnum = record[0]
#     if idnum not in custID:
#         num = 0
#         custID.append(idnum)
#         total = float(record[3]) + float(record[4]) + float(record[5])
#         sales.write(f'{idnum},  ')
#         # sales.write(f'{idnum},    ${total:10,.2f}\n')
#     elif idnum in custID:
#         nexttotal = float(record[3]) + float(record[4]) + float(record[5])
#         total = total + nexttotal
#         sales.write(f' ${total:10,.2f}\n')

###########################################################

# for record in csv_file:
#     idnum = record[0]
#     total = float(record[3]) + float(record[4]) + float(record[5])
#     if idnum not in custID:
#         custID.add(idnum)
#         sales.write(f'{idnum},  {total:10,.2f}\n')

# print(custID)


#########################################

# customer_totals = {}

# # Open the input file ("sales.csv") and read its contents
# with open('sales.csv', 'r') as infile:
#     reader = csv.reader(infile)

#     # Skip the header row in the input file
#     next(reader)

#     # Iterate through the rows in the input file
#     for row in reader:
#         customer_id = row[0]
#         sub_total = float(row[3])
#         tax_amt = float(row[4])
#         freight = float(row[5])
#         total = sub_total + tax_amt + freight

#         # If customer ID is already in the dictionary, add to the existing total
#         if customer_id in customer_totals:
#             customer_totals[customer_id] += total
#         else:
#             customer_totals[customer_id] = total

# # Open the output file ("salesreport.csv") and write the combined totals
# with open('salesreport.csv', 'w', newline='') as outfile:
#     writer = csv.writer(outfile)

#     # Write the header row to the output file
#     writer.writerow(['Customer ID', 'Total'])

#     # Write the combined totals for each customer ID to the output file
#     for customer_id, total in customer_totals.items():
#         writer.writerow([customer_id, round(total,2)])

#####################################################

# seen_customer_ids = set()

# # Open the input file ("sales.csv") and read its contents
# with open('sales.csv', 'r') as infile, open('salesreport.csv', 'w', newline='') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)

#     # Write the header row to the output file
#     writer.writerow(['CustomerID', 'Total'])

#     # Skip the header row in the input file
#     next(reader)

#     # Iterate through the rows in the input file
#     for row in reader:
#         customer_id = row[0]
#         sub_total = float(row[3])
#         tax_amt = float(row[4])
#         freight = float(row[5])
#         total = sub_total + tax_amt + freight

#         # Check if we've already seen this customer ID
#         if customer_id not in seen_customer_ids:
#             seen_customer_ids.add(customer_id)
#             writer.writerow([customer_id, total])

# print("Sales report generated successfully.")




#     if record[0] == '250':
#         a = float(record[3]) + float(record[4]) + float(record[5])
#         atotal += a
#         aa = record[0]
#     elif record[0] == '251':
#         b = float(record[3]) + float(record[4]) + float(record[5])
#         btotal += b
#         bb = record[0]
#     elif record[0] == '252':
#         c = float(record[3]) + float(record[4]) + float(record[5])
#         ctotal += c
#         cc = record[0]
#     elif record[0] == '253':
#         d = float(record[3]) + float(record[4]) + float(record[5])
#         dtotal += d
#         dd = record[0]
#     elif record[0] == '254':
#         e = float(record[3]) + float(record[4]) + float(record[5])
#         etotal += e
#         ee = record[0]
#     elif record[0] == '255':
#         f = float(record[3]) + float(record[4]) + float(record[5])
#         ftotal += f
#         ff = record[0]
#     elif record[0] == '256':
#         g = float(record[3]) + float(record[4]) + float(record[5])
#         gtotal += g
#         gg = record[0]
#     elif record[0] == '257':
#         h = float(record[3]) + float(record[4]) + float(record[5])
#         htotal += h
#         hh = record[0]
#     elif record[0] == '258':
#         i = float(record[3]) + float(record[4]) + float(record[5])
#         itotal += i
#         ii = record[0]
#     elif record[0] == '259':
#         j = float(record[3]) + float(record[4]) + float(record[5])
#         jtotal += j
#         jj = record[0]
#     elif record[0] == '260':
#         k = float(record[3]) + float(record[4]) + float(record[5])
#         ktotal += k
#         kk = record[0]
#     elif record[0] == '261':
#         l = float(record[3]) + float(record[4]) + float(record[5])
#         ltotal += l
#         ll = record[0]
    

# sales.write(f'{aa},    ${atotal:10,.2f}\n')
# sales.write(f'{bb},    ${btotal:10,.2f}\n')
# sales.write(f'{cc},    ${ctotal:10,.2f}\n')
# sales.write(f'{dd},    ${dtotal:10,.2f}\n')
# sales.write(f'{ee},    ${etotal:10,.2f}\n')
# sales.write(f'{ff},    ${ftotal:10,.2f}\n')
# sales.write(f'{gg},    ${gtotal:10,.2f}\n')
# sales.write(f'{hh},    ${htotal:10,.2f}\n')
# sales.write(f'{ii},    ${itotal:10,.2f}\n')
# sales.write(f'{jj},    ${jtotal:10,.2f}\n')
# sales.write(f'{kk},    ${ktotal:10,.2f}\n')
# sales.write(f'{ll},    ${ltotal:10,.2f}\n')
