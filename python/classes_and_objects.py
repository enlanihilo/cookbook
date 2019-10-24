"""
    #About Classes

       - Creating a new class creates a new type of object
         allowing new instances of that type to be made.

       - Each class instance can have attributes and methods.

       Class  = blueprint
       Object = instance of class (thing created from class)

    #variables

        variable:
            class variable. will be shared by all instances
        self.variable:
            unique variable to each instance

    #Inheritance

        Parent class
        -------------
           |- Child Class
           |- Child Class
        
        Child classes inherit methods and 
        variables from its Parent class.
"""

class Mammalia:
    anatomy = ["jaw joint", "middle ear", "occipital condyles", "sweat glands"]


#Inheritance
class Felidae(Mammalia):
    
    kingdom = "Animalia"
    family = "Felidae" 
    order = "Carnivora"
    phylum = "Chordata" 
    type_genus = "Felis"

    def print_stats(self):
        print("""\nFelidae is a family of mammals in the order Carnivora,\nColloquially referred to as cats, and constitutes a clade.\n""")
        print(f"kingdom = {self.kingdom}")
        print(f"family = {self.family}")
        print(f"order = {self.order}") 
        print(f"phylum = {self.phylum}")
        print(f"type genus = {self.type_genus}")

    def print_anatomy(self):
        print("Anatomy:")
        for i in self.anatomy:
            print(f"\t- {i}")

    
#Inheritance
class Felinae(Felidae):
    subfamily = "Felinae"
    
        
#Inheritance
class Felis(Felinae):

    def __init__(self, name):
        self.name = name


cat = Felis("Garfield")
cat.print_anatomy()
cat.print_stats()