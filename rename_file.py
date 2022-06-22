import os
import lewis_utilities

numbers = lewis_utilities.get_list_data_from_text("number.txt")

for number in numbers:
    number = number.strip()    
    old_name_file = "A:\\telegram_accounts\\" + number + "\\" + number + ".session"
    new_name_file = "A:\\telegram_accounts\\" + number + "\\" + "+" + number + ".session"
    os.rename(old_name_file, new_name_file)
    print("done rename " + old_name_file + " to " + new_name_file)
    old_name_folder = "A:\\telegram_accounts\\" + number
    new_name_folder = "A:\\telegram_accounts\\" + "+" + number
    os.rename(old_name_folder, new_name_folder)
    print("done rename folder " + old_name_folder + " to " + new_name_folder)
