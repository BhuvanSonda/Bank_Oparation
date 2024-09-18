import xlsxwriter as xlwriter
import time
st=time.time()
workbook=xlwriter.Workbook('inersert_imag2.xlsx')

sheet=workbook._add_sheet('image')



sheet.insert_image('I9', 'famer.jpg')

sheet.autofit()
workbook.close()
ed=time.time()
ttl=ed-st
print(ttl)