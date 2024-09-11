from openpyxl import Workbook
from openpyxl.styles import Color
from openpyxl.formatting.rule import ColorScaleRule

# Create a workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Add some sample data
for row in range(1, 11):
    ws.append([row])

# Define a three-color scale rule (minimum, midpoint, and maximum)
color_scale_rule = ColorScaleRule(start_type='percentile', start_color='00FF0000',
                                  mid_type='percentile', mid_value=50, mid_color='00FFFF00',
                                  end_type='percentile', end_color='0000FF00')

# Apply the color scale rule to a specific range of cells
ws.conditional_formatting.add('A1:XFD1048576', color_scale_rule)

# Save the workbook
wb.save('three_color_scale.xlsx')
