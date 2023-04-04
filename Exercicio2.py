import xml.dom.minidom as xml

arq = xml.parse('CysticFibrosis2-20230404/data/cf79.xml')

titles = arq.getElementsByTagName("TITLE")

doc = xml.Document()
root = doc.createElement('TITLES')

for text in titles:
    #print(text.firstChild.data)
    ch = doc.createElement('title')
    ch.appendChild(doc.createTextNode(text.firstChild.data))
    ch.data = text.firstChild.data
    root.appendChild(ch)


doc.appendChild(root)



file_handle = open("Resultado/titulos.xml", "w")
doc.writexml(file_handle, indent= '   ', newl= "\n")
file_handle.close()


