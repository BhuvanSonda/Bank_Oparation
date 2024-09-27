import os 
from datetime import datetime

today=datetime.now()# get the today date and time

def Add_File(file_name='.txt'):

    today=datetime.now()# get the today date

    today_date=today.strftime('%d-%m-%Y')
    folder_name=today_date

    # Create a new folder with the current date as the name
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)#create folder 
        print('Folder create Successfully')

# create and add file to the current folder
    file=today.strftime('%d-%m-%Y_%H_%M_%S_')+file_name
    file_path=os.path.join(folder_name,file)
    if not os.path.exists(file):
        with open(file_path,'w+')as file:
            pass
    # else:
    #     with open(file_path,'a')as file:
    #         pass
    return file_path
# file_name=''
# s=Add_File("Htm.html")
# print(type(s))