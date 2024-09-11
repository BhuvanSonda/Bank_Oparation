import openpyxl as xl

# Load the workbook and select the active sheet
wb = xl.load_workbook('save.xlsx')
sheet = wb.active
#to create font style 
cell_colr=xl.styles.Font(name="'Arial",bold=True,size=10,color='0A673D')
#to assign style to the fonts
sheet['A1'].font=cell_colr
sheet['B1'].font=cell_colr
sheet['C1'].font=cell_colr

#to make fill style
clr_fill=xl.styles.PatternFill(fill_type='solid',start_color='FFDF92',end_color='FFDF92')
#to fill the cell A1
sheet['A1'].fill=clr_fill



# Save the workbook with the changes
wb.save('save.xlsx')
