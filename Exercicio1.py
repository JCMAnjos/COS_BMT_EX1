import xml.etree.ElementTree as ET

xml = ET.parse('CysticFibrosis2-20230404/data/cf79.xml')
root = xml.getroot()

fileSave = ET.Element('AUTHORS')

for child in root.iter('AUTHOR'):
    author=ET.Element("AUTHOR_NAME")
    author.text = child.text
    fileSave.append(author)

tree = ET.ElementTree(fileSave)

ET.indent(fileSave)

tree.write('Resultado/autores.xml')

print(ET.tostring(fileSave, encoding='utf8').decode('utf8'))

