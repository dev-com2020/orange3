# import json
#
# import xmltodict
#
# with open("hello.svg") as xml_file:
#     data_dict = xmltodict.parse(xml_file.read())
#
# json_data = json.dumps(data_dict, indent=4)
#
# with open("nowe_dane.json", 'w') as json_file:
#     json_file.write(json_data)


import xml.etree.ElementTree as E

tree = E.parse('test.xml')
root = tree.getroot()
d = {}
for child in root:
    if child.tag not in d:
        d[child.tag] = []
    dic = {}
    for child2 in child:
        if child2.tag not in dic:
            dic[child2.tag] = child2.text
    d[child.tag].append(dic)
print(d)

# from xml.dom import minidom
#
# doc = minidom.parse('test.xml')
#
# print(doc.toxml())
# nodes = doc.childNodes
# for i in nodes[0].getElementsByTagName("osoba"):
#     print(i.getElementsByTagName("imie")[0].nodeName)
#     print(i.getElementsByTagName("imie")[0].childNodes[0].toxml())
#     print(i.getElementsByTagName("imie")[0].getAttribute("foo"))


# with open("hello.svg") as file:
#     doc = ET.parse(file)
#     root = doc.getroot()
#
#     for item in root.findall("defs"):
#         for child in item:
#             print(child)


# print(root)

# element = doc.getElementById("smiley")
# print(element.parentNode)
# print(element.firstChild)
