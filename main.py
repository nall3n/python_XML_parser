
from xml.etree import ElementTree

tree = ElementTree.parse('XML\TradeItemPrice_341220_20240502-145114-753.xml')

root = tree.getroot()

for item in root.findall('Item'):
    #print(item.tag)

    if item.find('DepositItem'):
        item_id = item.findall('ItemID')
        pant_price = item.find('DepositItem').find('Price').text
        pant_quantity = item.find('DepositItem').find('Quantity').text
        tax_rate = item.find('TaxRate').text
        pant_total_value = float(pant_price) * float(pant_quantity)
        for id in item_id:
            print(id.text, pant_price, pant_quantity, " total: ", pant_total_value, tax_rate)
    else: 
        pass




#from xml.dom.minidom import parse, parseString
#document = parse('XML\TradeItemPrice_341220_20240502-145114-753.xml')
#items = document.getElementsByTagName('Item')
#for item in items:
#    itemId_node =item.getElementsByTagName('ItemID')
#    print(itemId_node[0].nodeValue)
#    print(itemId_node[0])
