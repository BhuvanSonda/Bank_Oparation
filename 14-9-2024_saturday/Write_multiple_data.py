import xlsxwriter

# Create a workbook and add a worksheet
workbook = xlsxwriter.Workbook('Write_multiple_data2.xlsx')
worksheet = workbook.add_worksheet('data')

# Define your data (list of lists or similar structure)
data = [
    ['Name', 'Age', 'City'],
    ['Bhuvan', 20, 'Sirsi'],
    ['Santoshi', 18, 'Honnassdfghjdfgfghdfghdfxdfcgxcvar'],
    ['Rakshit', 19, 'Hubballi'],
    ['Rohan', 21, 'Dharwad'],
    ['mohan',25,'Madras'],
    ['Rohini', 22, 'Bangalore'],

]

# Write data to worksheet
row = 0
col = 0

for item in data:
    worksheet.write_row(row, col, item)
    row += 1

worksheet.autofit()
print("****There is no error in code!!****\n")
# Close the workbook
workbook.close()
