import xml.etree.ElementTree as ET
data = '''
    <person>
        <name> Tawheed </name>
        <phone type="intl">
            9103100145
        </phone>
        <email hide="yes"/>
    </person>
'''

tree = ET.fromstring(data)
#here we now search in the tree
print("Name :", tree.find('name').text)
print("Attribute :", tree.find('email').get('hide'))