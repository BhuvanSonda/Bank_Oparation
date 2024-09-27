
import pandas as pd
import openpyxl as xl

file = "pandas_and_openpyxl.xlsx"
# file_path = Add_File(file)

# Create a Pandas dataframe 
df = pd.read_excel(r"C:\Users\Docketrun\Desktop\Bhuvan_python_program.py\data.xlsx")

# Create a Pandas Excel writer 
writer = pd.ExcelWriter(file, engine="openpyxl")

# Add the dataframe to Excel 
df.to_excel(writer, sheet_name="Sheet1")

# Get the workbook and worksheet 
workbook = writer.book
worksheet = writer.sheets["Sheet1"]
(max_row, max_col) = df.shape

from openpyxl.formatting.rule import ColorScaleRule

# Define a three-color scale rule (minimum, midpoint, and maximum)
color_scale_rule = ColorScaleRule(start_type='min', start_color='00FF0000',
                                  mid_type='percentile', mid_value=50, mid_color='FFFF00',
                                  end_type='max',end_color='0000FF00')

# Apply the color scale rule to a specific range of cells
worksheet.conditional_formatting.add('D2:D1048576', color_scale_rule)
# Create a bar chart

chart = xl.chart.BarChart()

chart.title = "Bank Holders Balance Graph"
chart.x_axis.title = "A/C_No"
chart.y_axis.title = "Balance"

# Define the data for the chart
values =xl.chart. Reference(worksheet, min_col=4, min_row=1, max_col=4, max_row=max_row+1)
categories = xl.chart.Reference(worksheet, min_col=3, min_row=2, max_row=max_row+1)

# Add data and categories 
chart.add_data(values, titles_from_data=True)
chart.set_categories(categories)


# Add the chart position in sheet
worksheet.add_chart(chart, "L7")

writer.close()
print('Successfully Saved the changes')