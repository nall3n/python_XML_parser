import os
from os import path


xml_list = os.listdir(path.join(os.curdir,"XML"))
for i in xml_list:
    if not i.endswith(".xml"):
        xml_list.pop(xml_list.index(i))

for j in xml_list:
    print(j)


first_time = 953