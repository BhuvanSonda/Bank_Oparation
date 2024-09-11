import xlsxwriter

workbook = xlsxwriter.Workbook('exception.xlsx')

worksheet1 = workbook.add_worksheet('Sheet1')
worksheet2 = workbook.add_worksheet('sheet1')

workbook.close()
