from xml.etree import ElementTree
from datetime import date
import os
from os import path

brand_name = "testbrand"
profileId = "1"
pant_list = []
pant_articels = {
    1: 124235,
    2: 124,
    3: 12415,
    4: 15135,
    6: 41255,
    8: 15246357,
    12: 12314,
}
article_id_list = []
output_file = open("out%s.txt" % date.today(), "a")

xml_folder = "XML"
xml_list = os.listdir(path.join(os.curdir, xml_folder))
for i in xml_list:
    if not i.endswith(".xml"):
        xml_list.pop(xml_list.index(i))

for xml_file in xml_list:

    tree = ElementTree.parse(path.join(xml_folder, xml_file))
    root = tree.getroot()

    for item in root.findall('Item'):
        #print(item.tag)

        if item.find('DepositItem'):
            item_id = item.findall('ItemID')
            pant_price = item.find('DepositItem').find('Price').text
            pant_quantity = item.find('DepositItem').find('Quantity').text
            tax_rate = item.find('TaxRate').text
            pant_total_value = float(pant_price) * float(pant_quantity)
            if pant_total_value not in pant_list:
                pant_list.append(pant_total_value)
            for id in item_id:

                if id.text not in article_id_list:
                    article_id_list.append(id.text)
                    #print(id.text, pant_price, pant_quantity, " total: ", pant_total_value, tax_rate)
                    script_output = """ 
                    UPDATE truepos_brand_%s_posprofile_%s.article
                    SET APantId = %s WHERE Barcode = '%s';""" % (brand_name, profileId, pant_articels.get(pant_total_value) if pant_articels.get(pant_total_value) else "NULL" , id.text)
                    print(script_output)
                    output_file.writelines(script_output)

output_file.close()

for pant in pant_list:
    if pant in pant_articels:
        print("%f exists!" % pant)
    else:
        print("Warning: pant article for pant: %f is missing" % pant)

#from xml.dom.minidom import parse, parseString
#document = parse('XML\TradeItemPrice_341220_20240502-145114-753.xml')
#items = document.getElementsByTagName('Item')
#for item in items:
#    itemId_node =item.getElementsByTagName('ItemID')
#    print(itemId_node[0].nodeValue)
#    print(itemId_node[0])
