def get_list_data_from_text(directory):
    f = open(directory, "r")
    list_data = []
    for x in f:
        list_data.append(x)
    return list_data
def append_to_text_file(directory, content):    
    f = open(directory, "a", encoding="utf-8")    
    f.write(content + "\n")
    f.close()