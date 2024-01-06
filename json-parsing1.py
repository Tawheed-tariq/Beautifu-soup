import json
input = '''
    [
        {
            "id" : 1,
            "name" : "Tawheed"
        },
        {
            "id" : 2,
            "name" : "exceptme"
        }
    ]
'''

info = json.loads(input)
print("content len : ", len(info))

for item in info:
    print("name : ", item["name"])
    print("id : ", item["id"])