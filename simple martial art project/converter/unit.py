from dataclasses import dataclass

"""
dataclass decorator
- Used to ease the process of class creation, where the class has some
standard basic functionality.
- With dataclass you do not need to specify a __init__ method as you 
would do with a normal class.
- An object of the class can still be accessed through dot-notation.
- To pass the values to initialize the object we use th ekey value
pair. as arguments 


"""

@dataclass
class Unit:
    abbrev: str
    value_in_std_units: float


# object
gram = Unit(abbrev="g", value_in_std_units=0.001)
print(gram.value_in_std_units)