import xlsxwriter as xl
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname('create_folder.py')))

from create_folder import Add_File

file = "format.xlsx"
file_path = Add_File(file)

workbook=xl.Workbook(file_path)
sheet=workbook.add_worksheet("format1")

data=[
    ['Bhuvan', 50, "PUC_II"],
    ["Radha", 18, "SSLC"],
    ['Girija', 25, "B.Com"],
    ['Rahul', 22, "B.Sc"],
    ['Ramesh', 28, "MBA"],
    ['Sushan', 32, 'MBBS'],
    ['Suresh', 35, 'MCA'],
    ['Suraj', 35, 'MCA'],
    ['Suresh', 42, 'MBA'],
    ['Ragu', 24, 'SSLC'],
    ['Rajesh', 26, 'B.Com'],
    ['Raj', 23, 'B.Com'],
    ['Santhoshi', 23, 'PUC_II'],
]

heddings=['Name','Age','EDU']


format=workbook.add_format({'bg_color':'ffbf00',"align":"centre",'border':2})
align=workbook.add_format({'align':'centre','bg_color':'ffe6e6','border':2,'italic':True})

format.set_bold()

for headding in heddings:
    sheet.write(0, heddings.index(headding), headding, format)
row=1
col=0
# sheet.set_row(1,1048576,align)
# sheet.set_column('A:XFD',cell_format=align)
for name,age,edu in data:
    sheet.write(row, col, name,align)
    sheet.write(row,col+1,age,align)
    sheet.write(row,col+2,edu,align)
    row+=1

workbook.add_chartsheet('new_one')
workbook.set_tab_ratio(75)

workbook.close()
