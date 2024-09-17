import xlsxwriter as xlwriter

workbook=xlwriter.Workbook('Embed_imag.xlsx')
sheet=workbook._add_sheet('embed')
sheet.set_row(3, 120)
sheet.set_column(3,1,15)
sheet.insert_image(3,1,'famer.jpg', {'x_scale': 0.5, 'y_scale': 0.5})
workbook.close()