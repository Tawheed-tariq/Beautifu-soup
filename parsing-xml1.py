import xml.etree.ElementTree as ET
input = '''
    <stuff>
        <users>
            <user x="2">
                <name>
                    Tawheed
                </name>
                <id>
                    001
                </id>
            </user>
            <user x="7">
                <name>
                    Exceptme
                </name>
                <id>
                    002
                </id>
            </user>
        </users>
    </stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #finds all user tags inside of users tag
print('user content : ', len(lst) )

#parsing the list of trees
for item in lst:
    print("Name : ", item.find('name').text)
    print("Id : ", item.find('id').text)
    print("Attribute : ", item.get('x'))
