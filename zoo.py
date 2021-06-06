class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    def display_info(self):
        print(f" Nombre: {self.name}\n Salud: {self.health}\n Felicidad: {self.happiness}\n")
        return self
    def feeding(self):
        self.health += 10
        self.happiness += 10
        return self

class Eagle(Animal):
    def __init__(self, name, age, species, health=70, happiness=50):
        super().__init__(name, age, health, happiness)
        self.species = species

class Bear(Animal):
    def __init__(self, name, age, species, health=30, happiness=20):
        super().__init__(name, age, health, happiness)
        self.species = species

class Owl(Animal):
    def __init__(self, name, age, species, health=80, happiness=50):
        super().__init__(name, age, health, happiness)
        self.species = species

class Artiodactyl(Animal):
    def __init__(self, name, age, species, health=45, happiness=35):
        super().__init__(name, age, health, happiness)
        self.species = species

# Andres = Eagle('Andres', 5, 'Bald Eagle' )
# Andres.feeding().display_info()

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_Eagle(self, name, age, species):
        self.animals.append( Eagle(name, age, species) )
        return self
    def add_Bear(self, name, age, species):
        self.animals.append( Bear(name, age, species) )
        return self
    def add_Owl(self, name, age, species):
        self.animals.append( Owl(name, age, species) )
        return self
    def add_Artiodactyl(self, name, age, species):
        self.animals.append( Artiodactyl(name, age, species) )
        return self
    def print_all_info(self):
        print("-"*30, "The animals in the", self.name, "are:", "-"*30)
        for animal in self.animals:
            print(f"{animal.name}: a {animal.species}, whose health level is {animal.health} and whose happiness level is {animal.happiness}.")
metropolitan = Zoo("Metropolitan Zoo")
metropolitan.add_Eagle('Andres', 35, 'Bald Eagle')
metropolitan.add_Owl('Nala', 20, 'Barn Owl')
metropolitan.add_Artiodactyl('Shere Khan', 10, 'Vicuña')
metropolitan.print_all_info()











