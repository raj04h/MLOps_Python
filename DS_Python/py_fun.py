


# Function 
def double(x):
    """Doubles a number"""
    return x * 2

print(double(5)) # Prints 10

# Function with Arguments
def full_name(first, last):
    return first + " " + last

print(full_name("John", "Doe")) # Prints John Doe

# Variable Arguments
def sum_all(*numbers):
    sum = 0 # variable
    for n in numbers:
        sum += n
    return sum

print(sum_all(1, 2, 3)) # Prints 6

# Keyword Arguments
def greet(name, greeting="Hello"):
    print(greeting + ", " + name)

greet("John") # Prints Hello, John
greet("Mary", greeting="Hi") # Prints Hi, Mary


# Generator: A type of iterable like lists or tuples but does not store the full sequence in memory at once. 
# Uses yield to generate one item at a time

#counter generator
def counter(start=0):
    n=start
    while True:
        yield n  # prient
        n +=2

for i in counter(4):
    if i >20:
        break
    print(i)


# Generator expression: More compact syntax like list comprehensions for inline lazy generation
# uses () instead of []

nums=(x**2 for x in range(10))
print(list(nums))


# Infinite Sequence: Generators can be infinity
import random
attacks=["kimura", "armbar", "triangle"]

def lazy_random_attack():
    while True:
        attack=random.choice(attacks)
        print("Yielding attack")
        yield attack

generator=lazy_random_attack()
for _ in range(5):
    print(next(generator))


def simple_gen():
    yield 1
    yield 2
    yield 3

g = simple_gen()

print(next(g))  # ➤ 1
print(next(g))  # ➤ 2
print(next(g))  # ➤ 3

def lazy_return_random_attacks():
    """Yield attacks each time"""
    
    # Import random library
    import random
    
    # Dictionary of attacks mapped to body part
    attacks = {"kimura": "upper_body", 
               "straight_ankle_lock":"lower_body",
               "arm_triangle":"upper_body",
               "keylock": "upper_body",
               "knee_bar": "lower_body"}

    # Infinite loop 
    while True:
        # Get random attack 
        random_attack = random.choices(list(attacks.keys()))
        
        # Yield attack one at a time
        yield random_attack
        
# Create attack generator 
attack = lazy_return_random_attacks()

# Show it's a generator object
print(type(attack)) 

# Print 6 random attacks
for _ in range(6): 
    print(next(attack))

