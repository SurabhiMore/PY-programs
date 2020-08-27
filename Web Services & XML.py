# Python's xml package - ElementTree module - reads and manipulates(parses) XML(eXtensible Maarkup Language-used in webpages where data has specific srtucture)

import xml.etree.ElementTree as ET
data = ''' 
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes"/>
</person>'''

info = ET.fromstring(data)
print('Name:',info.find('name').text)
print('Attribute:',info.find('email').get('hide'))

import xml.etree.ElementTree as ET
info = '''
<stuff>
   <users>
      <user x="2">             # first element
          <id>001</id>
          <name>Chuck</name>   
      </user>
      <user x="7">             # second element
           <id>009</id>
           <name>Brent</name>
      </user>
   </users>
</stuff>'''

data = ET.fromstring(info)
print(data) # element 'stuff' at (address)
lst = data.findall('users/user')
print(lst)  # two elements -  element 'user' at (address)
print('User count:',len(lst))
for user in lst:                            # "user" is the iterating variable
    print('Name:',user.find('name').text)
    print('Id:',user.find('id').text)
    print('Attribute:',user.get('x'))