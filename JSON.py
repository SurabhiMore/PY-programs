# json module (JavaScript Object Notation)
# parsing JSON string by using json.loads() method - Python dictionary or list

import json
# dictionary (nested)
data = '''{                   
"name" : "Chuck",
"phone" : {
   "type" : "intl",
   "number" : "+1 734 303 4456"
   },
"email" : {
   "hide" : "yes"
   }
}'''
info = json.loads(data)        # dictionary
print('Name:',info['name'])
print('Hide:',info["email"]["hide"])

# dictionary as elements in LIST
input = '''[               
  {"id" : "001",
   "x" : "2",
   "name" : "Chuck"
  },
  {"id" : "009",
   "x" : "7",
   "name" : "Brent"
  }
]'''
info = json.loads(input)       # list
print('User count:',len(info))
for item in info:
    print('Name:',item["name"])
    print('Id:',item["id"])
    print('Attribute:',item["x"])

