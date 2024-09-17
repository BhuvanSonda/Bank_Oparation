import openpyxl as xl
from openpyxl.worksheet.table import Table, TableStyleInfo

# Create a workbook and select the active worksheet
wb = xl.Workbook()
ws = wb.active

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
ws.append(['Items', 'Price', 'Saled_pieces'])

# Add data to the worksheet
for row in data:
    ws.append(row)

# Define the table range (A1:C19) considering headers and data
tab = Table(displayName='Table_1', ref='A1:C19')

# Define the table style
style = TableStyleInfo(name="TableStyleMedium6", showFirstColumn=True,
                       showLastColumn=True, showRowStripes=True, showColumnStripes=True)

# Apply the table style to the table
tab.tableStyleInfo = style

# Add the table to the worksheet
ws.add_table(tab)

# Save the workbook to a file
wb.save("TABLE.xlsx")
