import json

with open('dummy.json', 'r') as f:
    data = f.read()
    jsonparsed = json.loads(data)   #deserializes JSON to a python object
    print(jsonparsed)
    #print(data)
