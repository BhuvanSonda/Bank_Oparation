import xlsxwriter as xlwriter
import sys
import os

# Adjust path to include directory containing create_folder.py
sys.path.insert(0, os.path.abspath(os.path.dirname('create_folder.py')))

import create_folder

# Rest of your code

import create_folder 

file='URL.xlsx'
file_path=create_folder.Add_File(file)
workbook=xlwriter.Workbook(file_path)
sheet=workbook._add_sheet('url')
sheet.write('A1','Sl.No')
sheet.write('B1','URL_links')
sheet.write('A2',1)
sheet.write('A3',2)
sheet.write_url('B2','https://docs.google.com/document/d/1hwwdg7d2dikITCulqt56scpAr-CC56WkS8ZwcVdo5Ek/edit')
sheet.write_url('B3','https://xlsxwriter.readthedocs.io/workbook.html')

grt_url=workbook.get_default_url_format()
sheet.write_url('B4',str(grt_url))
sheet.write('A4',4)
sheet.autofit()

workbook.close()