# User Input and While Loops!

# How the input() Function Works

# The input() function pauses you program and waits for the user to enter some text. Once Python receives the user's input, it assigns that input to a variable to make it convenient for you to work with.
message = input("Tell me something, and I will repeat it back to you:")
print(message)
# The input() function takes one argument : the prompt that we want to display to the user,so they know what kind of information to enter.

# Writing Clear Prompts
# Each time you use the input() function , you should include a clear , easy to follow prompt that tells the user exactly what kind of information you are looking for.
name = input("Please enter your name:")
print(f"\nHello,{name}!")

# sometimes you will want to write a prompt thats longer than one line .


ans = "If You share your name, we can personalize the messages you see."
ans+= "\nWhat is your First Name? "

name = input(ans)
print(f"\nHello,{name}!")
# This example shows one way to build a mutlilines string.
# The first line assigns the first part of the message to the variable prompt. In the second line, the operator += takes the string that was assigned to prompt and adds the new string onto the end.

# USing int() to Accept Numerical Input
# When you use the input() function, python interprets everything the user enters as a string. 

n= int(input("How old are you?"))
print(n)


height = int(input("Enter your height in inches:"))
if height >= 45:
    print("\nYou are Tall enough to Ride!")
else:
    print("\nYou will be able to ride when you are older a little more.")
    
# The MOdulo (%) Operator
# The Modulo % operator tells you what the remainder is.

number = int(input("Enter A Number, and I will Tell you if its even or odd?"))

if number % 2 == 0:
    print("\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
    
# Introducing While Loops
# The for Loop takes a collection of items and executes a block of code once for each item in the collection. Where as the while loop runs as longs as or while a certain conditon is true.

# The While Loop in Action

cur = 1
while cur <= 5:
    print(cur)
    cur += 1
    
# Letting the user choose when to quit
ans = "\nTell me something, and I will repeat it back to you:"
ans+= "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(ans)
    print(message)
    
# 1. We first define a prompt that tells the user their two options: A. Entering a message or B. entering the 'quit' value.
# 2. Then we set up a variable message to keep track of whatever value the user enters. We Define the message as an empty string."", so python has something to check the first time it reaches the while line.
# 3. The first time the programs runs and pythoon reaches the while statement, it needs to compare the value of message to 'quit'.

# Using A Flag

# For a program that should run only as long as many conditions are true , you can define one variable that determines whether or not the entire program is active.This is called FLAG.

ans = "\nTell me something, and I will repeat it back to you:"
ans+= "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(ans)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
        
# Using Break to Exit a Look
# The break statement directs the flow of your program, you can use it to control which lines of code are executed and which arent. so the program only executes code that you want it to,when you want it to.

ans = "\nPlease Enter the name of a city you have visited:"
ans+= "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(ans)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to{city.title()}!")
        
# NOTE: You can use the break statement in any of Python's loops. For example,you could use break to quit a for loop that's working through a dictionary or a list.

# Using CONTINUE in a Loop
# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop, based on the result of a conditonal test.

cur = 0
while cur < 10:
    cur += 1
    if cur %2 == 0:
        continue
    print(cur)
    
# 1.First we set cu to 0. because its less than 10. Python enters the loop. once inside the loop, we increment the count by 1.
# so current number is 1. the if statement then checks the modulo of cur and 2. if the modulo is 0(which means cur is divisile by 2), the continue statement tells the python to ignore the rest of the loop and return to the beginning. If the current number is not divisible b 2 , the rest of the loop is executed and python prints the current number.

# Avoiding Infinite Loops

x = 1
while x <= 5:
    print(x)
    x += 1      
    
x = 1
while x <= 5:
    print(x)
    
    # this loop will run forever.
    
# Using a while loop wwith lists and dictionaries

# Using while loops with lists and dictionaries allows you to collect,store and organize lots of input to examine and report on later.


# Moving Items from one List to Another

# Start with the users that need to be verified
# and an empty list to hold confirmed users.
unconfirmed_users = ['Rahul','Harsh','Subhajeet']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)
    
# Display all the current users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    
# Removing all instances of Specific Values from a List.

# we use remove() to remove a specific value from a list. The remove() function worked because the value we were interested in appeared only once in the list

names = ['Rahul','Subhajeet','Harsh','Shivam','Digendra','Pawan']

while name in names:
    names.remove('Shivam')
print(names)


# Filling a Dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("which mountain would you like to climb someday?")
    
    responses[name] = response
    
    repeat = input("Would you like to let another prson respond? (yes/no)")
    if repeat == "no":
        polling_active = False
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
    
# The program first defines an empty dictionary (responses) and sets a flag(polling_active) to indicate that polling is active. As long as polling_active is True. Python will run the code in the while loop.With in the loop , the user is prompted to enter their name and a mountain they would like to climb. 1 . that information is stored in the responses dictionary, and the user is asked whether or not to keep the pull running. 2 if they enter yes the program enters the while looop again . IF they enter no, the polling_active flag is set to false, the while loop stops running and the final code block 3 displays the result of the poll.


    