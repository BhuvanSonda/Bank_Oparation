import xlsxwriter as xlwriter

workbook=xlwriter.Workbook('inersert_imag2.xlsx')

sheet=workbook._add_sheet('image')



sheet.insert_image('I9', 'famer.jpg')

sheet.autofit()
workbook.close()