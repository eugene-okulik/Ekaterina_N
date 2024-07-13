import os

import datetime

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(base_path, "eugene_okulik", "hw_13", "data.txt")
print(file_path)
with open(file_path, encoding="utf-8") as file:
    for line in file:
        file_line = line.split(" - ")
        file_line1 = file_line[0].split(". ")
        date_str = file_line1[1]
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        if file_line1[0] == "1":
            date = date + datetime.timedelta(days=7)
            print(date)
        if file_line1[0] == "2":
            print(date.strftime("%A"))
        if file_line1[0] == "3":
            date_now = datetime.datetime.now()
            differ = date_now - date
            print(differ.days)
