import xlsxwriter as xl

#workbook=xl.Workbook("insert_button.xlsx")
# workbook=xl.Workbook("insert_button.xlsm")
workbook=xl.Workbook("insert_button.xlsb")#create workbook
sheet=workbook.add_worksheet('button')#ceate sheet


data = (['Bhuvan', 500, "PUC_II"],
        ["Radha", 180, "SSLC"],
        ['Girija', 250, "B.Com"],
        ['Rahul', 220, "B.Sc"],
        ['Ramesh', 280, "MBA"],
        ['Sushan', 320, 'MBBS'],
        ['Suresh', 350, 'MCA'],
        ['Suraj', 350, 'MCA'],
        ['Suresh', 420, 'MBA'],
        ['Ragu', 240, 'SSLC'],
        ['Rajesh', 260, 'B.Com'],
        ['Raj', 230, 'B.Com'],
        ['Santhoshi', 230, 'PUC_II'])

# Headings
headings = ['Name', 'Age', 'EDU']

# Define formatting
border = 2
format = workbook.add_format({"bold": True, 'bg_color': 'ffbf00', "align": "center", 'border': border})
align = workbook.add_format({'align': 'center', 'bg_color': '00ffff', 'border': border})

# Write headings to the worksheet
for heading in headings:
    sheet.write(0, headings.index(heading), heading, format)

# Write data to the worksheet
row = 1
col = 0
for name, age, edu in data:
    sheet.write(row, col, name, align)
    sheet.write(row, col + 1, age, align)
    sheet.write(row, col + 2, edu, align)
    row += 1


sheet.insert_button('E5',{'macro':"say hello",'caption':'press me'})#insert button
print('file run Successfully')#for refrence
workbook.close()#to save and colse the file