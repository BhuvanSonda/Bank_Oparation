import xlsxwriter as xl
import sys
import os
sys.path.insert(0,os.path.abspath(os.path.dirname('create_folder.py')))

from create_folder import Add_File

file='add_table.xlsx'
file_path=Add_File(file)

workbook=xl.Workbook(file_path)
sheet=workbook.add_worksheet('Table')
caption = "Table with user defined column headers."
data = [
    ["Apples", 10000, 5000, 8000, 6000],
    ["Pears", 2000, 3000, 4000, 5000],
    ["Bananas", 6000, 6000, 6500, 6000],
    ["Oranges", 500, 300, 200, 700],
]
# Set the columns widths.
sheet.set_column("B:G", 12)

# Write the caption.
sheet.write("B1", caption)

# Add a table to the worksheet.
sheet.add_table(
    "B3:F7",
    {
        "data": data,
        "columns": [
            {"header": "Product"},
            {"header": "Quarter 1"},
            {"header": "Quarter 2"},
            {"header": "Quarter 3"},
            {"header": "Quarter 4"},
        ],
    },
)

workbook.close()
