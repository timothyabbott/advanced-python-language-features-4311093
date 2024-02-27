from enum import Enum, auto
# Example file for Advanced Python: Language Features by Joe Marini
# define enumerations using the Enum base class


# TODO: enums have human-readable values and types
class Fruit(Enum):
    Apple = 1
    Banana = 2
    Pear = 3
    Plum = 4
    Grape = auto()

print(Fruit.Apple)
print(type(Fruit.Apple))
print(repr(Fruit.Apple))
# TODO: enums have name and value properties
print(Fruit.Apple.name, Fruit.Apple.value)

# TODO: print the auto-generated value
print(Fruit.Grape.value)
# TODO: enums are hashable - can be used as keys

my_fruits = {}
my_fruits[Fruit.Apple]="yum"
print(my_fruits.get(Fruit.Apple))
