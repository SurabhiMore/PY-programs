# Accessing dictionary elements

frnds = ['Milly','Silly','Lilly', 'Milly']
names = dict()
for frnd in frnds:
    names[frnd] = names.get(frnd,0) + 1   # dict[list] = dict(list element,0) + 1
print(names)   # dictionary of count

print(names.get('candy'))     # if only candy was passed then the output will be None as there is no such key
print(names.get('candy',-1))

person = {'name': 'Phill', 'age': 22}
print('Name: ', person.get('name'))   # .get() method
print(person['name'])                 # using bracket (disadvantage)

print('Age: ', person.get('age'))
# value is not provided
print('Salary: ', person.get('salary'))
# value is provided
print('Salary: ', person.get('salary', 0.0))
# square brackets[] :- Key Error is raised in case a key is not found in the dictionary.
