import xlsxwriter as xlw

workbook=xlw.Workbook('multiple_sheet.xlsx')#create workbook

sheet=workbook.add_worksheet('September')#create sheet in workbook

sheet2=workbook.add_worksheet('october')#create sheet in workbook

#initialize data
data=(
    ['Rent',5500],
    ['Grocery',500],
    ['Transportation',0],
    ['Entertainment',300],
    ['Miscellaneous',500],
    ['Medical',100],

)
#formate for bold
bold=workbook.add_format({'bold':True,"bg_color":"red"})

#headdings
sheet.write('A1','Expense',bold)
sheet.write('B1','Amount',bold)
sheet2.write('A1','Expense',bold)
sheet2.write('B1','Amount',bold)

row=1
col=0

#write all datas in xl file
for purpose,amount in data:
    sheet.write(row,col,purpose)
    sheet.write(row,col+1,amount)
    row+=1

#find the total expendature using formula
sheet.write(row,col,"Total")
sheet.write(row,col+1, "=SUM(B1:B6)")

#close the workbook
workbook.close()
