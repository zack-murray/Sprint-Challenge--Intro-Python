# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
# person name for person in humans if p.name starts with D
a = [p.name for p in humans if p.name.startswith('D')]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [p.name for p in humans if p.name.endswith("e")]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
# startswith(prefix[, start[, end]])
#c = [p.name for p in humans if p.name.startswith('C', 'G')]
#starts_with = ['C', 'D', 'E', 'F', 'G']
#c = [p.name for p in humans if (p.name[0] in starts_with)]
"""
>>> list(map(chr, range(97, 123))) #or list(map(chr, range(ord('a'), ord('z')+1)))
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
"""
c = [p.name for p in humans if p.name[0] in list(map(chr, range(ord('C'), ord('G')+1)))]
#c = [p.name for p in humans if p.name[0] in list(map(chr, range(99,103)))]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [(p.age + 10) for p in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
# only works if you convert age to str
e = [p.name + "-" + str(p.age) for p in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(p.name, p.age) for p in humans if p.age in range(27,33)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
# need to include human class from above 
g = [Human(p.name.upper(), p.age + 5) for p in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
# math.sqrt(x)
import math
h = [math.sqrt(p.age) for p in humans]
print(h)
