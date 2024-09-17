import xlsxwriter as xlwriter

# Create a workbook and worksheet
workbook = xlwriter.Workbook("xl_formula.xlsx")
sheet = workbook.add_worksheet("format1")

# Define the data to be written
data = (['Bhuvan', 500, 12],
        ["Radha", 180, 12],
        ['Girija', 250, 12],
        ['Rahul', 220, 12],
        ['Ramesh', 280, 12],
        ['Sushan', 320, 12],
        ['Suresh', 350, 12],
        ['Suraj', 350, 12],
        ['Suresh', 420, 12],
        ['Ragu', 240, 12],
        ['Rajesh', 260, 12],
        ['Raj', 230, 12],
        ['Santhoshi', 230, 12])



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

# Create a new chart sheet and add a column chart
chart_sheet = workbook.add_chartsheet('new_one')
chart = workbook.add_chart({'type': 'column'})

# Add series to the chart (from format1 worksheet)
chart.add_series({
    'categories': '=format1!$A$2:$A$14',  # X-axis categories (names)
    'values': '=format1!$B$2:$B$14',      # Y-axis values (ages)
    'name': "Marks"
})

# Set the chart in the chartsheet
chart_sheet.set_chart(chart)
formula=sheet.write_array_formula(1,3,13,3,'{B2:B14+C2:C14}',workbook.add_format({"bold": True, 'bg_color': 'bfff00', "align": "center", 'border': border}))

sheet.write('E1', None, format)  # write_blank()
sheet.write('E2', None) # Ignored

sheet.write_boolean('E3', True)
sheet.write_boolean('E4', False)

# Close the workbook to save it
workbook.close()
