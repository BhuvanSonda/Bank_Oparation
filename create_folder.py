
def Add_File(file_name):
    import os 
    from datetime import datetime

    today=datetime.now()
    today_date=today.strftime('%d-%m-%Y')
    folder_name=today_date
    # Create a new folder with the current date as the name
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print('Folder create Successfully')


    file_path=os.path.join(folder_name,file_name)
    with open(file_path,'w+')as file:

        pass
    return file_path
  