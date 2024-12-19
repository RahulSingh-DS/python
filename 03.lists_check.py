# A list is a collection of items in a particular order. 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
print(chocolates)

# Accessing Elements in the list
#[0,1,2,3,4] Its ranked this way!
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
print(chocolates[0])

# A special syntax for accessing the last element in a list. By asking for the item at index -1.
# [-5,-4,-3,-2,-1] Its Ranked this way!
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
print(chocolates[-1])

# Using Indiviual elements from the lists!
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
message = f"My favourite chocolate is {chocolates[-1].title()}"
print(message)

# Modifing the elements in the list
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates[0] = "Mango-Bite"
print(chocolates)

# Adding Elements to the list at the end using .append() function
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates.append("Coffee-Bite")
print(chocolates)

# Inserting Elements to the list 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates.insert(1,'Coconut Candy')
print(chocolates)

# Removing an Element from the list 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
del chocolates[1]
print(chocolates)

# Removing an Item Using the pop() Method 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates.pop(0)
print(chocolates)

# Removing Elements by Value 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates.remove("Nestle")
print(chocolates)

# Organizing the list 
# sorting the list 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates.sort()
print(chocolates)

# You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates.sort(reverse=True)
print(chocolates)

# Sorting a List Temporarily with the sorted() Function
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
print("Here is the Original List: ")
print(chocolates)

print("\nHere is the sorted list:")
print(sorted(chocolates))

print("\nHere is the Original List Again:")
print(chocolates)

# Printing the list in reverse order, it doesnt reverse alphabetic. 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
chocolates.reverse()
print(chocolates)

# Finding The length of the lists. 
chocolates = ["DairyMilk","Nestle","kinderJoy", "Kitkat", "5-star"]
len(chocolates)
print(chocolates)
