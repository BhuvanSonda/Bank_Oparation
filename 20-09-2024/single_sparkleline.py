import xlsxwriter as xl
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname('create_folder.py')))

from create_folder import Add_File

file = 'single_sparkle.xlsx'
file_path = Add_File(file)
workbook= xl.Workbook(file_path)
worksheet = workbook.add_worksheet()

# Sample data
data = [
    [10, 20, 15, 25, 30, 5, 40],
    [12, 3, 2, 1, 3, 1, 3],
    [3, 32, 1, 45, 2, 5, 10]
]

# Write data to the worksheet
for row_num, row_data in enumerate(data):
    worksheet.write_row(row_num, 0, row_data)  # Write each row of data

#  to set the type to line and add a title:
worksheet.add_sparkline('H4', {'range': 'A1:G3', 'type': 'column'})

# Close the workbook
workbook.close()
