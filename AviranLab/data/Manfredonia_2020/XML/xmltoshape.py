import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()
classification = sys.argv[1][6:13]
transcript = root.find("transcript")
id = transcript.attrib["id"]


shape_data = root.findtext(".//reactivity")

shapesplit = shape_data.split(',')
for i in range(len(shapesplit)):
    shapesplit[i] = shapesplit[i].lstrip()
    if shapesplit[i] == 'NaN':
        shapesplit[i] = 'nan'


print(f'> {id}_{classification}')

for pos in shapesplit:
    print(f'{pos} ', end='')

print()
