class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry= False
        self.mood = "happy"
        self.move = ""

    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s may have eaten too much." % self.name)
            self.mood= "lethargic"
# my_pet = Pet("Kooly", 5, "cat")
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Izzy", 6, "koala")
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
my_pet = Pet("Fido", 4, "dog")
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
my_pet.is_hungry = True
print("Is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feelings %s" % my_pet.mood)
