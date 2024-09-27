import xlsxwriter as xl
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.dirname('create_folder.py')))

from create_folder import Add_File 

file = "Write_data.xlsx"
file_path = Add_File(file)#create and  add file to the folder 

start_time=time.time()

workbook=xl.Workbook(file_path)#create workbook


sheet=workbook.add_worksheet('list')#create first sheet

headings=['Name','Roll_No','Marks']# headdings of the data
sheet.write_row(0,0,headings,workbook.add_format({'bold':True,'bg_color':'ffbf00',"align":"centre",'border':2}))#add data to the sheet1

list_data=[
    ['Bhuvan',20,842],
    ['Rohan',21,242],
    ['Aryan',19,742],
    ['Aman',20,142],
    ['Ram',34,642],
    ['Sahil',21,542],
    ['RaGu',30,142],
    ['Ramesh',41,342],
]
#upload the list data into excel file
for row ,row_data in enumerate(list_data):
    for col,col_data in enumerate(row_data):
        sheet.write(row+1,col,col_data,workbook.add_format({"align":"centre",'border':2}))

print(f'list data entry excution time : {time.time()-start_time} second\n')


sheet2=workbook.add_worksheet('Dict')#create second sheet

dict_data={
   'Name': ['Bhuvan','Rohan','Aryan','Aman','Rahul'],
   'Roll_No':[20,21,19,20,21],
   'Marks':[542,542,542,542,542]
}

col=0
#upload the dict data into excel file
for key,value in dict_data.items():
    sheet2.write(0,col,key,workbook.add_format({'bold':True,'bg_color':'ffe6e6',"align":"centre",'border':2}))
    sheet2.write_column(1,col,value,workbook.add_format({"align":"centre",'border':2}))
    col+=1
print(f'dictionary data entry excution time : {time.time()-start_time} second\n')
table_start_time=time.time()
sheet3=workbook.add_worksheet('Table')

data = [
    ["Apples", 10000, 5000, 8000, 6000],
    ["Pears", 2000, 3000, 4000, 5000],
    ["Bananas", 6000, 6000, 6500, 6000],
    ["Oranges", 500, 300, 200, 700],
]
# Set the columns widths.
sheet3.set_column("B:G", 12)

# Add a table to the worksheet.
sheet3.add_table(
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
print(f'table entry excution time : {time.time()-start_time} second\n')
workbook.close()

print(f'Total excution time : {time.time()-start_time} second\n')
print('File saved Successfully')