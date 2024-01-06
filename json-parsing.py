import json
data = '''{
    "name" : "chuck",
    "phone" : {
        "type" : "intil", 
        "number" : 9103100145
    },
    "email" : {
        "hide" : "yes"
    }
    }
'''

info = json.loads(data) #converts data into a structured object
print("Name : ", info["name"])
print("attribute : ", info["email"]["hide"])