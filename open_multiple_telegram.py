import os
import shutil
from time import sleep
from async_timeout import timeout
from pywinauto.application import Application

# app = Application(backend="uia").start("notepad.exe")
# app = Application(backend="uia").connect(title="Untitled - Notepad", timeout=100)
# #app.UntitledNotepad.print_control_identifiers()
# text_editor = app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
# text_editor.type_keys("Mai Hoang Long", with_spaces = True)

def get_list_data_from_text(directory):
    f = open(directory, "r")
    listData = []
    for x in f:
        listData.append(x)
    return listData

change_ip_program_directory = "D:\\Programming\\github\\change_dcom_ip_automatically\\dist\\main.exe"
numbers = get_list_data_from_text("number.txt")
directory = "D:\\Programming\\github\\appium_python_automation_tool\\telegram_accounts\\already_sell\\batch_50_1\\"
src_path = directory + "Telegram.exe"
app = Application()
count = 0
number_of_account_to_change = 5
for number in numbers:
    
    #change ip
    if count % number_of_account_to_change == 0:
        print("start change ip")
        os.startfile(change_ip_program_directory)
        sleep(15)
    number = number.strip()
    print("open number " + number)
    path = directory + number
    #os.mkdir(path)
    destination_path = path + "\\Telegram.exe"
    shutil.move(src_path, destination_path)
    app.start(destination_path)
    sleep(5)
    app.kill()
    shutil.move(destination_path, src_path)
    count += 1