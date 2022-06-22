import os
import shutil 

import lewis_utilities

numbers = lewis_utilities.get_list_data_from_text("number.txt")

path = "A:\\telegram_accounts\\anakin_7xmyu5\\"
for number in numbers:
    number = number.strip()
    content = "+" + number + "|3813"
    file_dir = "A:\\telegram_accounts\\+" + number + "\\info.txt"
    lewis_utilities.append_to_text_file(file_dir, content)
    # session_path = path + number + ".session"
    # folder_session_path = path + number
    # os.mkdir(folder_session_path)
    # shutil.move(session_path, folder_session_path)
    print("=> info: " + content)