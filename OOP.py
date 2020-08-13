class PartyAnimal:   # class class_name
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed',self.x)    # prints current value of x

an = PartyAnimal()         # object created which is stored in a variable
an.party()
an.party()
an = 42                    # destruction by reassigning
print('an contains',an)



class PartyAnimal:          # class class_name
    x = 0
    name = ""               # internal variable
    def __init__(self, z):      # construtor having additional parameter
        self.name = z                        # -used to set up object variables
        print(self.name,'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

s = PartyAnimal("Sally")     # 'Sally' is the z parameter
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()



class PartyAnimal:          # class class_name
    x = 0                          # 2 variables(attributes)
    name = ""              # internal variable
    def __init__(self, z):      # construtor having additional parameter    constructor-grab that name parameter
        self.name = z                        # -used to set up object variables
        print(self.name,'constructed')

    def party(self):            # function(method)
        self.x = self.x + 1
        print(self.name,'party count',self.x)
# Inheritance
class FootballFan(PartyAnimal):      # this extends PartyAnimal
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()         # for Jim party count 2
        print(self.name,'points',self.points)

s = PartyAnimal("Sally")     # 'Sally' is the z parameter
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()