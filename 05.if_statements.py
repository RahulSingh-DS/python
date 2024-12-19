# In this chapter we will learn to write conditional tests, which allows you to check any condition of interest. 
cars = ['audi','bmw','kia','tata','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
# Conditional tests 
# At the heart of every if statements is an expression that can be evaluated as True OR False and is called a CONDITIONAL TEST. Python uses the value True and False to DEcide whether the cide in an if statements  should be executed. IF a Conditional Test Evaluates to True, Pyhon Executes the code following the if statement. IF the test evaluates to False,python ignores the code following the if statement.

# Checking For Quality
cars = ['audi','bmw','kia','tata','toyota']
for car in cars:
    if car == 'audi':
        print(True)
        print(car.upper())
        
    else:
        print(False)
        print(car.title())
        
# Checking For Enquality 
# When you want to determine whether two values arenot equal. We can combine an exclamation point and an equal sign(!=). This exclamation point represents "not", as it does in many other programming languages.

cars = ['audi','bmw','kia','tata','toyota']
requested_car = 'mercedies'

if requested_car != 'cars':
    print("We Dont Hold Mercedies!")
    
    
# Numerical Comparisons 
age = 18
if age <= 55:
    print(False)
elif age >= 18:
    print(True)

# Checking Multiple Conditions
Rahul = 21
Radha = 18
if Rahul >= 20 and Radha >= 20:
    print(True)
False
Rahul = 21
Radha = 16
if Rahul >= 15 and Radha >= 15:
    print(True)
False

# Using OR to Check Multiple Conditions
Radha = 18
Rahul = 21
if Rahul >= 20 or Radha >= 20:
    print(True)
else:print(False)
if Rahul >= 18 or Radha >= 18:
    print(True)
else:print(False)
if Rahul >= 25 or Radha >= 25:
    print(True)
else:print(False)

# Checking Whether A Value is in a list 
requested_cars= ['audi','bmw','kia','tata','toyota']
if 'audi' in requested_cars:
    print(True)
else:print(False)
if 'xyz' in requested_cars:
    print(True)
else:print(False)

# Checking Whether A Value is not in a list
banned_users = ['aaksh','david','jhon','devin']
user = 'devin'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
    
# Boolean Expressions
# A Boolean Expression is just another name for a conditional test. A Boolean Expression is either True or False
game_active = True
can_edit = False

# IF Statements
n = int(input("Enter Your Age"))
if n >= 18:
    print("You are old enough to vote!")
    print("Have You Registered Your Name to vote yet?")
elif n <= 18:
    print("Sorry, You are too young to vote")
    print("Please register to vote as soon as you turn 18!")
else:
    pass

# Amusement Park
# Using Multiple Elif Blocks 

n = int(input("Enter Your Age"))

if n < 4:
    print("Your Entry Cost is 0 Rs.")
elif n < 18:
    print("Your Entry cost is 50 Rs.")
elif n < 60:
    print("Your Entry cost is 100 Rs.")
else:
    print("Your Entry Cost will be 150 Rs.")

# Testing Multiple Conditions
# Sometimes we should use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one conditions could be True and you want to act on every condition that is true.

# The Pizzeria Example
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'peperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\n Finished making your pizza!")

# Using IF Statements With Lists 
# Lets continue with the pizzeria example
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding{requested_topping}.")
print("\n Finished making your pizza!")
# The Output is straightforward because this code is just a simple for loop. 

# Now,we will be adding changes to our pizzeria. IF the pizzeria runs out of green peppers?
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
if requested_topping == 'green peppers':
    print("Sorry!, we are out of green peppes right now.")
else:
    print(f"Adding{requested_topping}")
print("\nFinished making your pizza!")

# The output shows that each requested topping is handled appropriately. 

# Checking That A list is not Empty.

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding{requested_topping}.")
    print("\n Finished making your pizza!")
else:
    print("Are You Sure you want a plain pizza?")
# This list is empty so it will print the else statement

# Using Multiple Lists
available_toppings = ['mushrooms', 'oives','green peppers','pepperoni','pineapple', 'extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding{requested_topping}")
    else:
        print(f"Sorry!, we dont have{requested_topping}")
print("\n Finished making your pizza")