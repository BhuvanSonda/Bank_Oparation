import openpyxl as xl
import sys
from openpyxl.worksheet.table import Table, TableStyleInfo
import os
import time

sys.path.insert(0,os.path.abspath(os.path.dirname('create_folder.py')))
from create_folder import Add_File

file='Speed_check.xlsx'
file_path=Add_File(file)
workbook=xl.Workbook()
sheet=workbook.active

st_time=time.time()
# Data to be added to the worksheet
data = [
    ['Monitor', 100, 200], ['Pc', 120, 254],
    ['Mouse', 150, 300], ['Keyboard', 180, 350],
    ['Headset', 200, 400], ['Speaker', 220, 450],
    ['Printer', 250, 500], ['Scanner', 280, 550],
    ['Webcam', 310, 600], ['Tablet', 340, 650],
    ['Laptop', 370, 700], ['Desktop', 400, 750],
    ['Notebook', 430, 800], ['Camera', 460, 850],
    ['Microphone', 490, 900], ['Router', 520, 950],
    ['Switch', 550, 1000], ['Modem', 580, 1050]
      ]
# Add column headers to the worksheet
sheet.append(['Items', 'Price', 'Saled_pieces'])

# Add data to the worksheet
for row in data:
    sheet.append(row)

# Define the table range (A1:C19) considering headers and data
tab = Table(displayName='Table_1', ref='A1:C19')

# Define the table style
style = TableStyleInfo(name="TableStyleMedium6", showFirstColumn=True,
                       showLastColumn=True, showRowStripes=True, showColumnStripes=True)

# Apply the table style to the table
tab.tableStyleInfo = style

# Add the table to the worksheet
sheet.add_table(tab)

ed_time=time.time()
t_time=ed_time-st_time
# Save the workbook to a file
workbook.save(file)
print(f'Data uploading time is :{t_time}Seconds')
