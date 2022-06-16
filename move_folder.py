import os
import shutil
from time import sleep
from async_timeout import timeout
from pywinauto.application import Application

def get_list_data_from_text(directory):
    f = open(directory, "r")
    listData = []
    for x in f:
        listData.append(x)
    return listData

static_folder = input("input static folder: ")
dynamic_folder = input("input dynamic folder: ")

numbers = get_list_data_from_text("number.txt")


for number in numbers:    
    number = number.strip()
    path_b = dynamic_folder + "\\" + number
    shutil.move(path_b, static_folder)
    print("move " + path_b + " to " + static_folder)