class Animal:
    def eat(self):
        print("The animal is eating")

    def walk(self):
        print("The animal is walking")

class Feline(Animal):
    def lick(self):
        print("The feline is licking its fur")

    # must not modify the inheritance method
    def eat(self):
        print("The feline eats its food")


class Lion(Feline):
    def roar(self):
        print("The lion is roaring loudly !!!")


class Person:
    def watches(self, animal: Animal):
        animal.eat()

john = Person()
animal = Animal()
feline = Feline()
lion = Lion()

# the return should not be different for all classes that inherited it
john.watches(animal)
john.watches(feline)
john.watches(lion)