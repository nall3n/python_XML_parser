from xml.etree import ElementTree
from datetime import date
from time import sleep
import os
import json
from os import path

xml_folder = "XML STORAGE"
article_list_matrix = []

xml_list = os.listdir(path.join(os.curdir, xml_folder))
for i in xml_list:
    if not i.endswith(".xml"):
        xml_list.pop(xml_list.index(i))

# Generate two lists of article id / Barcodes 
for xml_file in xml_list:
    print(xml_file)
    tree = ElementTree.parse(path.join(xml_folder, xml_file))
    root = tree.getroot()

    article_list = []
    for item in root.findall('Item'):
        item_id = item.findall('ItemID')
        for id in item_id:
            # print(id.text)
            article_list.append(id.text)
    article_list_matrix.append(article_list)

matches = set(article_list_matrix[1]).intersection(article_list_matrix[0])

row_count = 0 
for row in matches:
    row_count = row_count +1 
    print(row)

print(row_count)
