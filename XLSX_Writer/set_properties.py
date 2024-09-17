import xlsxwriter as xlwriter

workbook=xlwriter.Workbook('set_properties.xlsx')

workbook.set_properties({
    'title':    'Set_Properties_Check',
    'subject':  'Properties_Check',
    'author':   'Bhuvan',
    'manager':  'Veera Raghavan',
    'company':  'DocketRun',
    'category': 'Filmy',
    'keywords': 'practice, python, xlsxwriter',
    'comments': 'Created with Python and XlsxWriter',
})

# Add some data to a worksheet.
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Hello')

workbook.set_size(200,500)
# Close the workbook.
workbook.close()

