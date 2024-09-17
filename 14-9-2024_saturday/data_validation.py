import xlsxwriter as xl

workbook=xl.Workbook('data_validation.xlsx')
sheet=workbook.add_worksheet('validation')

# sheet.data_validation('A1:XFD1048576',{'validate':'integer',
#                                        'criteria':'between',
#                                        'minimum':1,
#                                        'maximum':100})
sheet.data_validation('A1:XFD1048576',{'validate':'list',
                                       'source':['Bhuvan','santoshi','Rakshit','Rohini',10,100],
                                       'input_message':'choose any one'})#Validation criteria
print("****There is no error in code!!****\n")
workbook.close()