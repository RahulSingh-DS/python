# Understanding dictionaries allows you to model a variety of real_world objects more accurately.You will be able to create a dictionary representing a person and then store as much information as you want about that person.
# You can store their name, age ,location, profession and any other aspect of person you can describe.

# example
alien_0 = {'color':'green','points':5}

print(alien_0['color'])     # will return green
print(alien_0['points'])    # will return 5


# Working with Dictionaries

# A Dictionary in python is a collection of key-value pairs. Each key is connected to a value and you can use a key to access the value associated with that key. A Key's value can be a number,a string,a list or even another dictionary.
# A dictionary is wrapped in braces({}) with a series of key_value pairs inside the braces.
alien_0 = {'color':'green','points':5}

# A key value pair is a set of values associated with each other. When you provide a key,python returns the value associated with that key. Every key is connected to its value by a colon,and individual key_value pairs are separated by commas. You can store as many key_values pairs as you want in a dictionary.
alien_0= {'color':'green'}
# The String 'color' is a key in this dictionary and its associated value is 'green'.

# Accessing Values in a dictionary.
alien_0 = {'color':'green'}
print(alien_0['color'])    #return green

# now if a player shoots down the alien you can earn coins.

alien_0={'color':'green','points':5}

new_points = alien_0['points']
print(f"You just earned{new_points}points!")

# Adding New Key-value Pairs.
# Dictionaries are dynamic structures and you can add new key-value pairs to a dictionary at any time. 
    # - To add new key-value pair, you would give the name of the dictionay followed by the new key in square brackets,along with the new value.
#    - Lets add two new pieces of information to the alien_0 dictionary:
#       - the alien's x and y cordinates , which will help us display the alien at a particular position on the screen.
#       - Lets place the alien on the left edge of the screen, 25 pixels down from the top.

alien_0= {'color':'green','points':'5'}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting with an Empty Dictionary

# Its sometimes convenient or even necessary to start with an empty dictionary and then add each new item to it. To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line. Example:

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in Dictionaries
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key. Example

alien_0= {'color':'green'}
print(f"the alien is {alien_0['color']}.")   # The alien is green
alien_0['color'] = 'yellow'
print(f"the alien is now{alien_0['color']}.")   # The alien is yellow now.

# Another example , lets track the position of an alien that can move at different speeds. We 'll store a value representing the alien's current speed and then use it to determine how far to the right the alien should move:

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f"Original position:{alien_0['x_position']}")
# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']== 'medium':
    x_increment = 2
else:
    alien_0['speed'] == 'fast'
    x_increment = 3     #This must be a fast alien.
    
# The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New Position:{alien_0['x_position']}")


# Removing Key-Value Pairs
# When you no longer need a piece of information that's stored in a dictionary, you can use the del statement to completely remove a key-value pair.

# Lets remove the key'points' from thje alien_0 dictionary along with its value.

alien_0 = {'color':'green','points':5}
del alien_0['points']
print(alien_0)

# NOTE : BE AWARE THAT THE DELETED KEY-VALUE PAIR IS REMOVED PERMANENTLY.

# A Dictionary of similar objects

# You can also use a dictionary to store one kind of information about many objectives.

favorite_lang = {'Rahul':'Python','Shub':'C++','Harsh':'Java','Digendra':'React'}

# NOTE: Most editors have some functionality that helps you format extended lists and dictionary in a similar manner to this example. Other acceptable ways to format long dictionaries are available as well, so you may see slightly different formatting in your editor or in other sources.
favorite_lang = {'Rahul':'Python','Shub':'C++','Harsh':'Java','Digendra':'React'}
lang= favorite_lang['Rahul'].title()
print(f"Rahul's favourite language is {lang}")

# USing Get() to access Values

#  if the key 'points' exists in the dictionary , you will get the corresponding value. If it doesnt you get the default value.

alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('points','No point value assigned.')

print(point_value)

# NOTE: If you leave out the second argument in the call to get() and the key doesnt exist, Python will return the value NONE. The special Value NONE means"no value exists." this is not an error, its a special value meant to indicate the absecnce of a value.

# LOOPING THROUGH A DICTIONARY
# you can loop through all of a dictionary's key-value pairs, through its keys,or through its values.

user_0 = {'username':'Rabsvs', 'first':'Rahul','last':'Singh'}
# FOr creating loops you can create namees for the variables that will hold the key and value in each key-value pair. You can choose any names you want for these two variables.
for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"Value:{value}")


favorite_lang = {'Rahul':'Python','Shub':'C++','Harsh':'Java','Digendra':'React'}

for name , language in favorite_lang.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
    
    
# Looping Through all the keys in a dictionary
# THe keys () method is useful when you dont need to work with all of the values in a dictionary.

favorite_lang = {'Rahul':'Python','Shub':'C++','Harsh':'Java','Digendra':'React'}

for name in favorite_lang.keys():
    print(name.title())
    
    
# Looping Through all values in a dictionary 
favorite_lang = {'Rahul':'Python','Shub':'C++','Harsh':'Java','Digendra':'React'}

print("The Following languages have been mentioned:")
for language in favorite_lang.values():
    print(language.title())
    
# NOTE: You can build a set directly using braces and separating the elements with commas.

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.   
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens:{len(aliens)}")

# A LIST in a Dictionary
# Rather than putting a dictionary inside a list, its sometimes useful to put a list iniside a dictionary.

# Store Information about a pizza being ordered 
pizza = {
    'curst' :'thick',
    'toppings' : ['mushrooms','extra cheese'],
}

# Sumaarize the order
print(f"You ordered a {pizza['crust']}-crust pizza", "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
    
# NOTE: You should not nest lists and dictionaries too deeply. If you're nesting items much deeper than what you see in the preceding examples, or if you are working with someone else's code with significant levels of nesting, there's most likely a simpler way to solve the problem.

# A Dictionary in a Dictionary
# You can nest a dictionary inside another dictionary but your code can get complicated quickly when you do.

users = {
    'RahulSingh':{
        'first' : 'Rahul',
        'last': 'Singh',
        'location':'Raipur',
    },
    'Harsh':{
        'first':'Harsh',
        'last':'Dewangan',
        'location':'Bhilai'
    },
    
}

for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")
    
