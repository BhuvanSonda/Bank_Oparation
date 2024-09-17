import xlsxwriter as xlwriter

# Create a workbook and worksheet
workbook = xlwriter.Workbook("xl_writer_format.xlsx")
sheet = workbook.add_worksheet("format1")

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

# Close the workbook to save it
workbook.close()
