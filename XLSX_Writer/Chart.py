import xlsxwriter as xlwriter

workbook=xlwriter.Workbook('chart_xlwrtr.xlsx')
sheet=workbook.add_worksheet('chart')

# Define the data to be written
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

row=0
col=0
for name,marks,edu in data:
    sheet.write(row,col,name)
    sheet.write(row,col+1,marks)
    sheet.write(row,col+2,edu)
    row+=1

chart=workbook.add_chart({'type':'column'})
chart.add_series({
    'categories': '=chart!$A$1:$A$14',  # X-axis categories (names)
    'values': '=chart!$B$1:$B$14',      # Y-axis values (ages)
    'name': "Marks"
})
sheet.insert_chart('E1',chart=chart)

workbook.close()