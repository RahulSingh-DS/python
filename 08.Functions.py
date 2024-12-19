# You will learn to store functions in separate files called modules to help organize your main program files.

def greet_user(): 
    print("Hello")
greet_user()

# This example shows the simplest structure of a function. The first line uses the keyword def to inform Python that you are defining a function. This is the function definition. 

# Passing Information to a Function.

def greet_user(username):
    print(f"Hello,{username.title()}")

greet_user('Rahul')

# Arguments and Parameters
# the variable username in the definition of greet_user() is an example of a parameter.
# An argument is a piece of information that's passed from a function call to a function.

# NOTE: people sometimes speak of arguments and parameters interchangerbly . Dont be surprised if you see the variables in a function defintion referred to as arguments or the variables in a function call referred to as parameters. 

# Passing Arguments
# You can pass arguments to your functions in a number of ways. You can use positional arguments, which need to be in the same order the parameters were written. Keyword Arguments,  where each arguments consists of a variable name and a value and lists and dictionaries of values.

# Positional Arguments
#  When you call a function , python must match each arguments in the function call with a parameter in the function definition. The Simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments.

def describe_pet(animal_type,pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My{animal_type}'s name is {pet_name.title()}.")
    
describe_pet('cat','khushi')

# Multiple Function Calls

describe_pet('dog','harsh')

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so, when you pass the argument to the function, there's no confusion. keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.
describe_pet(animal_type='hamster',pet_name = 'harry')
describe_pet(pet_name='harry',animal_type='hamster')

# NOTE: When you use keyword arguments, be sure to use the exact names of the parameters in the function's definition.

# Default Values

# you can define a default value for each parameter,IF an argument for a parameter is provided in the function call.Python uses the argument value. IF not, it uses the parameter's default value.

# NOTE: When you use default values, any parameter with a default value needs to be listed after all the parameters that dont have default values. This Allows Python to continue interpreting positional arguments correctly.

# Equivalent Function Calls
# because positional arguments,keyword arguments and default values can all be used together, you will often have several equivalent ways to call a function.

#A dog named Harsh.
describe_pet('Harsh')
describe_pet(pet_name='harsh')

# Return Values
# A function doesnt always have to display its output directly. Instead it can process some data and then return a values. The value the function returns is called a return value.The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow you to move much of your program's grunt work into functions,which can simplify the body of your program.

# Returning a Simple Value
def get_name(first_name, last_name):
    full_name= f"{first_name} {last_name}"
    return full_name.title()
coder = get_name('Rahul','singh')
print(coder)

# A function for first,middle,last name

def get_names(first_name,middle_name='', last_name=''):
    if middle_name:
        full_name = f"{first_name}{middle_name}{last_name}"
    else:
        full_name = f"{first_name}{last_name}"
    
coder = get_name('rahul','singh')
print(coder)

# Returning a Dictionary

# A Function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.

def build_person(first_name, last_name):
    person = {'first':first_name,'last':last_name}
    return person
coder = build_person('rahul','singh')
print(coder)
# Example the following change allows you to store a person's age as well.
def build_person(first_name, last_name,age= None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
coder= build_person('rahul','singh', age = 21)
print(coder)

# Using a Function with a while loop
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name}{last_name}"
    return full_name.title()

# This is an infinite loop!
# while True:
    print("\nPLease Tell me your name:")
    f_name= input("First name")
    l_name = input("Last name")
    
    form_name = get_formatted_name(f_name,l_name)
    print(f"\nHello,{form_name}")


# Passing a List
# You will often find it useful to pass a list to a function, whether it's a list of names, numbers or more complex objects, such as dictionaries. When you pass a list to a function, the function gets direct access to the contents of the list. Lets use functions get direct access to the contents of the list.

def get_users(name):
    for name in names:
        msg = f"Hello,{name.title()}"
        print(msg)
        
usernames= ['rahul','harsh','don','subh','pawan']
greet_user(usernames)

# Modifying a List in a Function.

# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function's body are permanent, allowing you to work efficiently even when you are dealing with large amounts of data.

# Start with some designs that need to be printed.
unprinted_designs = ['phone case','robot pendant','dodecahedron']

completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)
    
# Display all completed models.
print("\nThe Following models have been printed:")
for completed_model in completed_models:
    print(completed_model) 
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

    
# Preventing a Function from Modifying A List

# function_name(list_name[:])

# Passing an Arbitrary Number of Arguments

# Sometimes you wont know ahead of time how many arguments a function needs to accept. Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.

#  the * asterik in the toppings tells python to make a tuple called toppings.
def make_pizza(*toppings):
    # Summarize the pizza we are about to make
    print("\nmaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
        
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# Mixing positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition.

def make_pizza(size,toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    
    for topping in toppings:
        print(f"-{topping}")
        
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

# NOTE: You will often see the generic parameter name *args , which collects arbitrary positional arguments like this.

# Using Arbitrary Keyword Arguments

# Sometimes you will want to accept an arbitrary number of arguments,but you wont know ahead of time what kind of information will be passed to the function.


def build_profile(first,last,**user_info):
    
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('rahul','singh',location='raipur',field = 'Datascience')

print(user_profile)

# NOTE: You will often see the parameter name **kwargs used to collect nonspecific keyword arguments.

