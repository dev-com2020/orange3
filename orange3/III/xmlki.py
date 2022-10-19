from xml.dom import minidom

doc = minidom.parse('test.xml')

print(doc.toxml())
nodes = doc.childNodes
for i in nodes[0].getElementsByTagName("osoba"):
    print(i.getElementsByTagName("imie")[0].nodeName)
    print(i.getElementsByTagName("imie")[0].childNodes[0].toxml())
    print(i.getElementsByTagName("imie")[0].getAttribute("foo"))


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


