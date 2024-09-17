
import xlsxwriter

# Create a new workbook and add a worksheet
workbook = xlsxwriter.Workbook('text_box.xlsx')
sheet = workbook.add_worksheet('textBox')

# Define the format for the text box background
fill = workbook.add_format({'bg_color': 'ffbf00'})

# Add a text box to the worksheet with the specified format
sheet.insert_textbox('E6', 'You can add any text here', {'x_scale': 1, 'y_scale': 1, 'font_size': 12, 'bg_color': 'ffbf00'})
sheet.set_column(0,4,20)
sheet.set_row(5,120)
# Close the workbook
workbook.close()
