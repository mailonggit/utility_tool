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

number = input("input number to open: ")
directory = "A:\\telegram_accounts\\"
src_path = directory + "Telegram.exe"
app = Application()
path = directory + number
destination_path = path + "\\Telegram.exe"
shutil.move(src_path, destination_path)
app.start(destination_path)
end = input("input ok to close telegram: ")
app.kill()
shutil.move(destination_path, src_path)