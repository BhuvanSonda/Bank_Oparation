import xlsxwriter as xl
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname('create_folder.py')))

from create_folder import Add_File

file = 'add_sparkle.xlsx'
file_path = Add_File(file)
wb = xl.Workbook(file_path)

sheet = wb.add_worksheet('sparkles')

data = [[5, 2, 9, -1, 0],
        [3, 4, 0, 6, 8],
        [5, 6, -3, 2, 0],
        [8, 5, 3, 0, -1]]

# Write data to the sheet
row = 0
for Row in data:
    sheet.write_row(row, 0, Row)
    row += 1

# Add sparklines for each row of data
sheet.add_sparkline('F1',{'range':'sparkles!A$1:E1','type':'line'})
sheet.add_sparkline('F2',{'range':'sparkles!A$2:E2','type':'column'})
sheet.add_sparkline('F3',{'range':'sparkles!A$3:E3','type':'win_loss'})
sheet.add_sparkline('F4',{'range':'sparkles!A$4:E4','type':'line'})
sheet.add_sparkline('F5',{'range':'sparkles!A$5:E5','type':'line'})


# Close the workbook
wb.close()
print("file Saved Successfully")