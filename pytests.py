import os
from os import path
import csv
import sys
import json

# xml_list = os.listdir(path.join(os.curdir,"XML"))
# for i in xml_list:
#     if not i.endswith(".xml"):
#         xml_list.pop(xml_list.index(i))

# for j in xml_list:
#     print(j)
# first_time = 953

xml_folder = "XML"

with open("trade_item_files.json", encoding="UTF-8") as f:
    
    data = json.load(f)

    for row in data:
        if row.get("Data"):
            print (row.get("Name"))
            with open(path.join(xml_folder, row["Name"]), 'w', encoding="UTF-8") as xml_file:
                xml_file.write(row["Data"])
        else:
            print ("File empty")