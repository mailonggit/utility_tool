import os
import shutil 

def get_list_data_from_text(directory):
    f = open(directory, "r")
    listData = []
    for x in f:
        listData.append(x)
    return listData

numbers = get_list_data_from_text("number.txt")
path = "A:\\telegram_accounts\\anakin_7xmyu5\\"
for number in numbers:
    number = number.strip()
    session_path = path + number + ".session"
    folder_session_path = path + number
    os.mkdir(folder_session_path)
    shutil.move(session_path, folder_session_path)
    print("=> move " + session_path + " to " + folder_session_path)