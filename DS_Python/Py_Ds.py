# List
nums= [1, 2, 3]
print(nums[2])

for n in nums:
    print (n)

# Tupple
colors=("red", "blue", "white", "black")
print(colors[0])

for clr in colors:
    print(clr)

# Dictionary
airports={"Del":"Delhi", "pat":"Patna", "Ban":"Banglore"}
print(airports)
print(airports["Ban"])

for code in airports: 
  print(airports[code])

# MEMBERSHIP check with IN  
print("SFO" in airports) # True, has key


# Set
unique_code={"SFO", "LAX", "SFO", "DEL"}
print(len(unique_code))
unique_code.pop()
# METHOD to add items
unique_code.add("ORD")


# List operations
fruits = ['apple', 'orange']
veggies = ['carrots', 'celery']

# append
fruits.append('banana') 
print(fruits) # ['apple', 'orange', 'banana']

# insert
fruits.insert(0, 'grapes')  
print(fruits) # ['grapes', 'apple', 'orange', 'banana']

# extend
fruits.extend(veggies)
print(fruits) # ['grapes', 'apple', 'orange', 'banana', 'carrots', 'celery'] 

# pop
removed = fruits.pop(2) 
print(removed) # orange
print(fruits) # ['grapes', 'apple', 'banana', 'carrots', 'celery']

# get
dict = {'name': 'Mary'}
print(dict.get('age', 25)) # 25 (default used)
