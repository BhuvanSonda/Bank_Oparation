
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname('create_folder.py')))

from create_folder import Add_File

file = "pandas_chart.xlsx"
file_path = Add_File(file)

# Create a Pandas dataframe 
df = pd.DataFrame({"Data": [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer 
writer = pd.ExcelWriter(file_path, engine="xlsxwriter")

# Add the dataframe to Excel 
df.to_excel(writer, sheet_name="Sheet1")

# Get the workbook and worksheet 
workbook = writer.book
worksheet = writer.sheets["Sheet1"]

# Create a chart
chart = workbook.add_chart({"type": "column"})

# Get the dimensions of the dataframe.
(max_row, max_col) = df.shape

# Configure the series of the chart from the dataframe data.
chart.add_series({"values": ["Sheet1", 1, 1, max_row, 1]})

# Insert the chart into the worksheet.
worksheet.insert_chart(1, 3, chart)

# Close the Pandas Excel writer 
writer.close()