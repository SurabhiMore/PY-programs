# Python's xml package - ElementTree module (XML processor API)

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
      <user x="2">             # first list element
          <id>001</id>
          <name>Chuck</name>   
      </user>
      <user x="7">             # second list element
           <id>009</id>
           <name>Brent</name>
      </user>
   </users>
</stuff>'''

data = ET.fromstring(info)
lst = data.findall('users/user')
print('User count:',len(lst))
for user in lst:
    print('Name:',user.find('name').text)
    print('Id:',user.find('id').text)
    print('Attribute:',user.get('x'))