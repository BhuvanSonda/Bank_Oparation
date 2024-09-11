import xlsxwriter as xlwriter

workbook=xlwriter.Workbook("xl_writer_format.xlsx")
sheet=workbook.add_worksheet("format1")

data=(['Bhuvan',20,"PUC_II"],
      ["Radha",18,"SSLC"])
heddings=['Name','Age','EDU']

border=2
format=workbook.add_format({"bold":True,'bg_color':'ffbf00',"align":"centre",'border':border})
align=workbook.add_format({'align':'centre','bg_color':'00ffff','border':border})

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

workbook.close()
