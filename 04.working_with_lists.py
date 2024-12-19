# We are learning loops in lists 
members = ["Rahul", "Radha", "Aadya", "Ansh", "Aahan"]
for member in members:
    print(member)
    
# Doing more work within the loops.
members = ["Rahul", "Radha", "Aadya", "Ansh", "Aahan"]
for member in members:
    print(f"{member.title()},we are family.")
    print(f"{member.title()}, we will be togeher!")
# Doing something after the loop ends 
print("Radha and Rahul loves you everyone!")

# Making Numerical Lists
# Using the range() function 
for value in range(1,5):
    print(value)
    
# Using range() values to make a list of numbers
numbers = list(range(1,6))
print(numbers)

# We can also use the range() function to tell to skip numbers in a given range. 
even_numbers = list(range(2,11,2))
print(even_numbers)

# (**) represent exponents. 
squares = []
for value in range(1,11):
    square= value ** 2
    squares.append(square)
    
print(squares)
'''
1. We start with an empty list called squares.
2. We Tell Python to Loop through each value from 1 to 10 using the range() function. Inside the loop, the current value is raised to the second power assigned to the variable square.
3. Each New Value of Square is appended to the list squares.
4. Finally , when the loop has finished running, the list of squares is printed.[1,4,9,16,25,36,49,64,81,100]
'''

# To write this code more cocinesly, omit the temporary variable square and append each new value directly to the list. 

squares = []
for value in range(1,11):
    squares.append(value** 2)

print(squares)

# Simple Statistics with a list of numbers.
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))

print(max(digits))

print(sum(digits))
