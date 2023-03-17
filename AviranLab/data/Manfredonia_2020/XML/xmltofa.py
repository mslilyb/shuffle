import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()
classification = sys.argv[1][6:13]
transcript = root.find("transcript")
id = transcript.attrib["id"]


shape_data = root.findtext(".//sequence")

shapesplit = shape_data.splitlines()
#print(shapesplit)
for i in range(len(shapesplit)):
    shapesplit[i] = shapesplit[i].lstrip().rstrip()
    if shapesplit[i] == 'NaN':
        shapesplit[i] = 'nan'

    if shapesplit[-1] == '':
        shapesplit.pop()

#print(shapesplit)

print(f'> {id}_{classification}')

for pos in shapesplit:
    print(f'{pos}', end='')

print()
